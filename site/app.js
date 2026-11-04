/* Course player. Reads site/data.json (compiled by scripts/render_board.py) and the Markdown briefs. */
(() => {
  // Served from /site/ locally (repo root one level up) or from the Pages root (content copied alongside).
  const IN_SITE = /\/site\/?(index\.html)?$/.test(location.pathname);
  const ROOT = IN_SITE ? "../" : "./";
  const DATA = IN_SITE ? "data.json" : "data.json";

  const $ = (s) => document.querySelector(s);
  let D = null;           // data.json
  let view = null;        // {stage, rung} | {doc}
  const mdCache = new Map();

  marked.setOptions({ gfm: true, breaks: false, headerIds: false, mangle: false });

  // ---------- helpers ----------
  const stageNum = (id) => String(parseInt(id.slice(1), 10));
  const allRungs = () => D.stages.flatMap((s) => s.parts.flatMap((p) => p.rungs.map((r) => ({ s, r }))));
  const findStage = (id) => D.stages.find((s) => s.id === id);
  const stateIcon = { locked: "", ready: "", in_progress: "", feedback: "", revising: "", passed: "✓ " };
  const stateTag = { locked: "locked", ready: "ready", in_progress: "now", feedback: "feedback", revising: "revising", passed: "passed" };

  function ring(frac, passed) {
    const r = 11.5, c = 2 * Math.PI * r, dash = Math.max(0, Math.min(1, frac)) * c;
    const label = passed ? "✓" : `${Math.round(frac * 100)}`;
    return `<svg class="ring" viewBox="0 0 28 28"><circle class="track" cx="14" cy="14" r="${r}"/><circle class="fill" cx="14" cy="14" r="${r}" stroke-dasharray="${dash} ${c}"/><text x="14" y="14">${label}</text></svg>`;
  }

  // ---------- left pane ----------
  function renderSide() {
    const c0 = D.course || {};
    document.title = `${c0.title || "Course"} ${c0.title_em || ""} · ${c0.org || ""}`.trim();
    $("#course-title").innerHTML = `${c0.title || "Course"}${c0.title_em ? ` <em>${c0.title_em}</em>` : ""}<span class="dot">.</span>`;
    const org = $("#org"); org.textContent = c0.org || ""; org.href = c0.org_url || "#";
    $("#tagline").textContent = c0.tagline || "";
    $("#learner").textContent = `${D.learner} · ${D.curriculum_version}`;
    $("#eyebrow").textContent = `Curriculum · ${D.stages.length} stages · ${D.hours_total} h`;
    const frac = D.hours_total ? D.hours_done / D.hours_total : 0;
    $("#overall-fill").style.width = `${Math.round(frac * 100)}%`;
    $("#overall-text").textContent = `${D.stages_passed} of ${D.stages.length} stages passed · ${D.hours_done} / ${D.hours_total} h`;
    $("#updated").textContent = `Board updated ${D.updated}`;

    const c = D.current;
    const btn = $("#continue");
    if (c && c.rung) {
      btn.innerHTML = `<span class="arrow">→</span>Continue · Stage ${stageNum(c.stage)}, Rung ${c.rung.n}<small>${c.rung.title}${c.rung.minutes ? ` · ~${c.rung.minutes} min` : ""}</small>`;
      btn.onclick = () => (location.hash = `#/${c.stage}/r${c.rung.n}`);
    } else if (c) {
      btn.innerHTML = `Stage ${stageNum(c.stage)} complete<small>File STAGE_FEEDBACK.md</small>`;
      btn.onclick = () => (location.hash = `#/${c.stage}`);
    } else {
      btn.textContent = "No stage in progress";
    }

    const tree = $("#tree");
    tree.innerHTML = "";
    for (const [tier, tname] of Object.entries(D.tiers)) {
      const h = document.createElement("div");
      h.className = "tier eyebrow";
      h.textContent = `Tier ${tier} — ${tname}`;
      tree.appendChild(h);
      for (const s of D.stages.filter((x) => x.tier === tier)) tree.appendChild(stageNode(s));
    }
  }

  function stageNode(s) {
    const el = document.createElement("div");
    el.className = `stage ${s.learner}` + (s.learner === "in_progress" ? " current" : "");
    el.dataset.id = s.id;
    const sub = s.rungs_total
      ? `${s.rungs_done} / ${s.rungs_total} rungs · ${s.hours} h`
      : `${s.hours} h · ${s.learner === "locked" ? "not yet rung-numbered" : s.learner_label}`;
    el.innerHTML = `
      <div class="stage-row">
        ${ring(s.fraction, s.learner === "passed")}
        <div><div class="stage-name">${stateIcon[s.learner]}Stage ${stageNum(s.id)} · ${s.name}<span class="chev">▶</span></div>
        <div class="stage-sub">${sub}</div></div>
        <div class="stage-hours ${s.learner}">${stateTag[s.learner]}</div>
      </div>
      <div class="rungs"></div>`;
    const rungs = el.querySelector(".rungs");
    if (!s.parts.length) {
      rungs.innerHTML = `<div class="empty">Outline only — the rungs are written one stage ahead of you. <a href="#/${s.id}">Read the brief</a></div>`;
    }
    for (const p of s.parts) {
      if (p.id) {
        const ph = document.createElement("div");
        ph.className = "part";
        ph.textContent = `Part ${p.id} — ${p.title}`;
        rungs.appendChild(ph);
      }
      for (const r of p.rungs) {
        const re = document.createElement("div");
        re.className = "rung" + (r.done ? " done" : "") + (r.current ? " current" : "");
        re.dataset.stage = s.id; re.dataset.rung = r.n;
        re.innerHTML = `<span class="mark">${r.done ? "✓" : r.current ? "▶" : "○"}</span><span class="rung-title">Rung ${r.n} — ${r.title}</span><span class="mins">${r.minutes ? r.minutes + " min" : ""}</span>`;
        re.onclick = (e) => { e.stopPropagation(); location.hash = `#/${s.id}/r${r.n}`; };
        rungs.appendChild(re);
      }
    }
    el.querySelector(".stage-row").onclick = () => {
      el.classList.toggle("open");
      if (!view || view.stage !== s.id) location.hash = `#/${s.id}`;
    };
    return el;
  }

  function syncSide() {
    document.querySelectorAll(".stage").forEach((el) => {
      const isView = view && view.stage === el.dataset.id;
      if (isView) el.classList.add("open");
    });
    document.querySelectorAll(".rung").forEach((el) => {
      el.classList.toggle("active", !!(view && view.stage === el.dataset.stage && view.rung === el.dataset.rung));
    });
  }

  // ---------- right pane ----------
  async function fetchMd(path) {
    if (mdCache.has(path)) return mdCache.get(path);
    const res = await fetch(ROOT + path);
    if (!res.ok) throw new Error(`${res.status} ${path}`);
    const txt = await res.text();
    mdCache.set(path, txt);
    return txt;
  }

  function slug(text) {
    return text.toLowerCase().replace(/[^\w\s-]/g, "").trim().replace(/\s/g, "-");
  }

  // Rewrite relative .md links to in-app routes; add ids to headings; mark rungs.
  function postProcess(container, basePath, stage) {
    const baseDir = basePath.includes("/") ? basePath.slice(0, basePath.lastIndexOf("/") + 1) : "";
    container.querySelectorAll("a[href]").forEach((a) => {
      const href = a.getAttribute("href");
      if (/^(https?:|mailto:|#)/.test(href)) { if (!href.startsWith("#")) a.target = "_blank"; return; }
      const [p, frag] = href.split("#");
      const resolved = normalize(baseDir + p);
      if (resolved.endsWith(".md") || resolved.endsWith("/")) {
        const target = resolved.endsWith("/") ? resolved + "README.md" : resolved;
        const m = target.match(/^stages\/(\d\d)-[^/]+\/README\.md$/);
        if (m) {
          const st = findStage(`s${m[1]}`);
          const rr = frag && st ? st.parts.flatMap((p) => p.rungs).find((x) => x.anchor === frag) : null;
          a.setAttribute("href", `#/s${m[1]}${rr ? "/r" + rr.n : ""}`);
        } else {
          a.setAttribute("href", `#/doc/${target}${frag ? "#" + frag : ""}`);
        }
      } else {
        a.setAttribute("href", ROOT + resolved); a.target = "_blank";
      }
    });
    container.querySelectorAll("h1,h2,h3,h4").forEach((h) => {
      const m = h.textContent.match(/^Rung (\w+) — /);
      h.id = slug(h.textContent);
      if (m && stage) {
        const r = stage.parts.flatMap((p) => p.rungs).find((x) => x.n === m[1]);
        if (r) {
          if (r.done) h.classList.add("is-done");
          if (r.current) h.classList.add("is-current");
          // Check card after the "**Check**" paragraph of this rung
          let el = h.nextElementSibling;
          while (el && !/^H[1-3]$/.test(el.tagName)) {
            if (el.tagName === "P" && el.textContent.trim() === "Check") {
              const card = document.createElement("div");
              card.className = "check-card";
              card.innerHTML = `<div class="row"><span class="${r.run ? "ok" : "no"}">${r.run ? "☑" : "☐"} Run</span><span class="${r.see ? "ok" : "no"}">${r.see ? "☑" : "☐"} See</span><span class="${r.say ? "ok" : "no"}">${r.say ? "☑" : "☐"} Say</span><span class="hint" style="margin:0 0 0 auto">${r.id}</span></div><div class="hint">Tick these in <a href="#/doc/PROGRESS.md">PROGRESS.md</a> with the minutes spent; the board re-renders on commit.</div>`;
              el.after(card);
              break;
            }
            el = el.nextElementSibling;
          }
        }
      }
    });
  }

  function normalize(p) {
    const out = [];
    for (const seg of p.split("/")) {
      if (seg === "..") out.pop(); else if (seg !== "." && seg !== "") out.push(seg);
    }
    return out.join("/");
  }

  function renderNow() {
    const n = D.now;
    $("#now").innerHTML = `<b>Now — ${n.headline}.</b> ${n.detail}<div class="next"><b>Next</b> &nbsp;${n.next}</div>`;
  }

  async function show() {
    const content = $("#content");
    renderNow();
    try {
      if (view.doc) {
        const md = await fetchMd(view.doc);
        content.innerHTML = marked.parse(md);
        postProcess(content, view.doc, null);
        $("#crumbs").innerHTML = `<b>${view.doc}</b>`;
        $("#now").style.display = "none";
        $("#prev").disabled = $("#next").disabled = true;
        if (view.frag) document.getElementById(view.frag)?.scrollIntoView();
        else $("#main").scrollTo(0, 0);
      } else {
        const s = findStage(view.stage);
        if (!s || !s.brief) throw new Error("No brief for " + view.stage);
        const md = await fetchMd(s.brief);
        content.innerHTML = marked.parse(md);
        postProcess(content, s.brief, s);
        $("#now").style.display = s.learner === "in_progress" ? "" : "none";
        const r = view.rung ? s.parts.flatMap((p) => p.rungs).find((x) => x.n === view.rung) : null;
        const part = r ? s.parts.find((p) => p.rungs.includes(r)) : null;
        const pill = r ? `<span class="pill ${r.done ? "done" : r.current ? "current" : ""}">${r.done ? "done" : r.current ? "you are here" : "not started"}</span>`
                       : `<span class="pill ${s.learner}">${s.learner_label}</span>`;
        $("#crumbs").innerHTML = `Tier ${s.tier} › <b>Stage ${stageNum(s.id)} · ${s.name}</b>` + (part && part.id ? ` › Part ${part.id}` : "") + (r ? ` › <b>Rung ${r.n}</b>` : "") + pill;
        const flat = allRungs();
        const idx = r ? flat.findIndex((x) => x.s.id === s.id && x.r.n === r.n) : -1;
        $("#prev").disabled = idx <= 0;
        $("#next").disabled = idx < 0 || idx >= flat.length - 1;
        $("#prev").onclick = () => { const t = flat[idx - 1]; location.hash = `#/${t.s.id}/r${t.r.n}`; };
        $("#next").onclick = () => { const t = flat[idx + 1]; location.hash = `#/${t.s.id}/r${t.r.n}`; };
        if (r) document.getElementById(r.anchor)?.scrollIntoView();
        else $("#main").scrollTo(0, 0);
      }
    } catch (e) {
      content.innerHTML = `<div class="err">Could not load: ${e.message}. Serve the repository root (e.g. <code>just site</code>) and open <code>/site/</code>.</div>`;
    }
    syncSide();
  }

  function route() {
    const h = location.hash.replace(/^#\/?/, "");
    if (!h) {
      const c = D.current;
      location.hash = c ? (c.rung ? `#/${c.stage}/r${c.rung.n}` : `#/${c.stage}`) : `#/${D.stages[0].id}`;
      return;
    }
    if (h.startsWith("doc/")) {
      const [path, frag] = h.slice(4).split("#");
      view = { doc: path, frag };
    } else {
      const [stage, rung] = h.split("/");
      view = { stage, rung: rung ? rung.replace(/^r/, "") : null };
    }
    show();
  }

  fetch(DATA).then((r) => r.json()).then((d) => {
    D = d;
    renderSide();
    window.addEventListener("hashchange", route);
    route();
  }).catch((e) => {
    $("#content").innerHTML = `<div class="err">Could not load data.json (${e.message}). Run <code>python scripts/render_board.py</code>, then serve the repo root.</div>`;
  });
})();
