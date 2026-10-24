// Shared header, footer, icons and interactions for every page.
const BIZ = {
  name: 'CCK Support',
  phone: '01227 668 041',
  tel: '+441227668041',
  email: 'info@ccksupport.co.uk',
  address: 'Building 1, 10 Wealden Forest Park, Herne Common, Herne Bay, Kent CT6 7LQ',
  facebook: 'https://www.facebook.com/ccksupport',
  cqc: 'https://www.cqc.org.uk/location/1-3099563436'
};

const ICONS = {
  phone: '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
  mail: '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
  pin: '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
  clock: '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
  check: '<circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/>',
  arrow: '<path d="M5 12h14M13 6l6 6-6 6"/>',
  menu: '<path d="M3 6h18M3 12h18M3 18h18"/>',
  close: '<path d="M6 6l12 12M18 6 6 18"/>',
  heart: '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21.2l8.8-8.8a5.5 5.5 0 0 0 0-7.8z"/>',
  home: '<path d="M3 10.5 12 3l9 7.5V21a1 1 0 0 1-1 1h-5v-7H9v7H4a1 1 0 0 1-1-1z"/>',
  hand: '<path d="M18 11V6a2 2 0 0 0-4 0v5M14 10V4a2 2 0 0 0-4 0v6M10 10.5V6a2 2 0 0 0-4 0v8"/><path d="M18 8a2 2 0 1 1 4 0v6a8 8 0 0 1-8 8h-2c-2.8 0-4.5-.9-6-2.4l-3.6-3.6a2 2 0 0 1 2.8-2.8L7 15"/>',
  brain: '<path d="M9.5 2A2.5 2.5 0 0 0 7 4.5v.1A3 3 0 0 0 4.5 8 3 3 0 0 0 3 10.6a3 3 0 0 0 1 4.9A3 3 0 0 0 7 19.5 2.5 2.5 0 0 0 9.5 22H12V2z"/><path d="M14.5 2A2.5 2.5 0 0 1 17 4.5v.1A3 3 0 0 1 19.5 8a3 3 0 0 1 1.5 2.6 3 3 0 0 1-1 4.9 3 3 0 0 1-3 4A2.5 2.5 0 0 1 14.5 22H12V2z"/>',
  bed: '<path d="M2 4v16M2 8h18a2 2 0 0 1 2 2v10M2 17h20"/><path d="M6 8v9"/>',
  cart: '<circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.7 13.4a2 2 0 0 0 2 1.6h9.7a2 2 0 0 0 2-1.6L23 6H6"/>',
  users: '<path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
  shield: '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
  pill: '<path d="M10.5 20.5 3.5 13.5a5 5 0 0 1 7-7l7 7a5 5 0 0 1-7 7z"/><path d="m8.5 8.5 7 7"/>',
  sun: '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
  moon: '<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>',
  quote: '<path d="M3 21c3 0 7-1 7-8V5H3v7h4c0 4-2 5-4 5zM14 21c3 0 7-1 7-8V5h-7v7h4c0 4-2 5-4 5z"/>',
  fb: '<path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/>',
  card: '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/>',
  key: '<circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6M15.5 7.5l3 3L22 7l-3-3"/>'
};
const icon = (n, cls = '') => `<svg class="${cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${ICONS[n] || ''}</svg>`;

// One list drives the service cards on the home page and the services page.
const SERVICES = [
  { id: 'personal', icon: 'heart', title: 'Personal care', text: 'Help with washing, bathing, dressing, toileting and skin, hair and nail care, always done with dignity.' },
  { id: 'medication', icon: 'pill', title: 'Medication support', text: 'Collecting prescriptions and help taking medication safely and on time.' },
  { id: 'home', icon: 'home', title: 'Help around the home', text: 'Meals, washing up, laundry, ironing, cleaning, shopping and even a bit of gardening.' },
  { id: 'company', icon: 'users', title: 'Companionship', text: 'A sit in service, a cuppa and a chat, trips out, social events and help to get to appointments.' },
  { id: 'complex', icon: 'brain', title: 'Complex and specialist care', text: 'Mental health support, brain injury, learning and physical disability, dementia and more.' },
  { id: 'respite', icon: 'sun', title: 'Respite and family relief', text: 'Give family carers a proper break, knowing their loved one is in safe, familiar hands.' }
];

const NAV = [
  ['index', 'Home', 'index.html'],
  ['services', 'Services & prices', 'services.html'],
  ['team', 'Our team', 'team.html'],
  ['contact', 'Contact', 'contact.html']
];

function header(page) {
  const links = NAV.map(([id, label, href]) => `<li><a href="${href}" class="${id === page ? 'active' : ''}">${label}</a></li>`).join('');
  return `
  <div class="topbar"><div class="wrap">
    <div class="tb-left">
      <span>${icon('pin')} Herne Bay, Whitstable &amp; nearby</span>
      <span class="tb-hide">${icon('clock')} Office Mon to Fri, 8am to 5pm</span>
    </div>
    <a href="mailto:${BIZ.email}" class="tb-hide">${BIZ.email}</a>
  </div></div>
  <header class="site-header"><div class="wrap nav">
    <a class="logo" href="index.html" aria-label="CCK Support home">
      <span class="logo-mark">${icon('heart')}</span>
      <span><b>CCK Support</b><small>Community care in Kent</small></span>
    </a>
    <ul class="menu" id="menu">${links}</ul>
    <div class="nav-cta">
      <a class="nav-phone" href="tel:${BIZ.tel}"><span class="ic">${icon('phone')}</span><span><small>Call the office</small>${BIZ.phone}</span></a>
      <a class="btn btn-primary" href="contact.html">Free assessment</a>
      <button class="burger" aria-label="Open menu" aria-expanded="false">${icon('menu')}</button>
    </div>
  </div></header>`;
}

function footer() {
  return `
  <footer class="site-footer"><div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="logo" href="index.html"><span class="logo-mark">${icon('heart')}</span><span><b>CCK Support</b><small>Community care in Kent</small></span></a>
        <p>A local, family run home care agency helping people in Herne Bay, Whitstable and the villages around them live safely and happily at home since 2012.</p>
        <a class="cqc-pill" href="${BIZ.cqc}" target="_blank" rel="noopener"><i></i> Rated Good by the CQC</a>
      </div>
      <div>
        <h4>Pages</h4>
        <ul>${NAV.map(([, l, h]) => `<li><a href="${h}">${l}</a></li>`).join('')}<li><a href="team.html#careers">Careers</a></li></ul>
      </div>
      <div>
        <h4>Care</h4>
        <ul>${SERVICES.map(s => `<li><a href="services.html#${s.id}">${s.title}</a></li>`).join('')}</ul>
      </div>
      <div>
        <h4>Get in touch</h4>
        <ul>
          <li><a href="tel:${BIZ.tel}">${BIZ.phone}</a></li>
          <li><a href="mailto:${BIZ.email}">${BIZ.email}</a></li>
          <li>${BIZ.address}</li>
          <li><a href="${BIZ.facebook}" target="_blank" rel="noopener">Facebook</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; ${new Date().getFullYear()} CCK Support Limited. All rights reserved.</span>
      <span>Office Mon to Fri 8am to 5pm, out of hours service available</span>
    </div>
  </div></footer>
  <a class="float-call" href="tel:${BIZ.tel}">${icon('phone')} Call us</a>`;
}

function serviceCards(withLinks) {
  return SERVICES.map((s, i) => `
    <article class="card reveal d${i % 3 + 1}">
      <div class="ic">${icon(s.icon)}</div>
      <h3>${s.title}</h3>
      <p>${s.text}</p>
      ${withLinks ? `<a class="more" href="services.html#${s.id}">Find out more ${icon('arrow')}</a>` : ''}
    </article>`).join('');
}

document.addEventListener('DOMContentLoaded', () => {
  const page = document.body.dataset.page;
  document.getElementById('site-header').outerHTML = header(page);
  document.getElementById('site-footer').outerHTML = footer();
  document.querySelectorAll('[data-services]').forEach(el => { el.innerHTML = serviceCards(el.dataset.services === 'links'); });
  document.querySelectorAll('[data-icon]').forEach(el => { el.innerHTML = icon(el.dataset.icon); });
  document.querySelectorAll('[data-tel]').forEach(el => { el.href = 'tel:' + BIZ.tel; });

  // Mobile menu
  const burger = document.querySelector('.burger'), menu = document.getElementById('menu');
  burger.addEventListener('click', () => {
    const open = menu.classList.toggle('open');
    burger.setAttribute('aria-expanded', open);
    burger.innerHTML = icon(open ? 'close' : 'menu');
  });

  // Header shadow on scroll
  const hdr = document.querySelector('.site-header');
  const onScroll = () => hdr.classList.toggle('scrolled', scrollY > 10);
  onScroll(); addEventListener('scroll', onScroll, { passive: true });

  // Headline words fade up one after another
  document.querySelectorAll('[data-split]').forEach(h => {
    let i = 0;
    const walk = node => [...node.childNodes].forEach(n => {
      if (n.nodeType === 3) {
        const frag = document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach(part => {
          if (!part.trim()) { frag.append(part); return; }
          const s = document.createElement('span');
          s.className = 'word'; s.textContent = part; s.style.animationDelay = (0.1 + i++ * 0.07) + 's';
          frag.append(s);
        });
        n.replaceWith(frag);
      } else walk(n);
    });
    walk(h);
  });

  // Reveal on scroll + counters
  const io = new IntersectionObserver(entries => entries.forEach(e => {
    if (!e.isIntersecting) return;
    e.target.classList.add('in');
    e.target.querySelectorAll('[data-count]').forEach(countUp);
    io.unobserve(e.target);
  }), { threshold: 0.15 });
  document.querySelectorAll('.reveal').forEach(el => io.observe(el));
  // Fast jumps (anchor links, quick flicks) can skip past elements; reveal anything already above the fold
  const catchUp = () => document.querySelectorAll('.reveal:not(.in)').forEach(el => {
    if (el.getBoundingClientRect().top < innerHeight) {
      el.classList.add('in'); el.querySelectorAll('[data-count]').forEach(countUp); io.unobserve(el);
    }
  });
  addEventListener('scroll', catchUp, { passive: true });

  function countUp(el) {
    const end = +el.dataset.count, suffix = el.dataset.suffix || '';
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) { el.textContent = end + suffix; return; }
    const t0 = performance.now(), dur = 1400;
    const tick = t => {
      const p = Math.min((t - t0) / dur, 1);
      el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }

  // Demo form: no backend yet
  document.querySelectorAll('form[data-demo]').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault();
    f.querySelector('.form-ok').classList.add('show');
    f.reset();
  }));
});
