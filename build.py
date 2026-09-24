#!/usr/bin/env python3
"""Builds index.html and descuento/index.html from one template.
Run:  python3 build.py
Only two images are used: the Transform Trauma México 2027 logo (inline SVG) and the speakers photo (inline WebP).
The Plus Jakarta Sans subset in assets/ loads separately with font-display:swap, so the page renders
immediately with a system font and upgrades when the font arrives.
"""
import base64, re, os, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
def read(p): return open(os.path.join(HERE, p), encoding='utf-8').read()

WA_NUMBER = '12133489759'
WA_MSG = 'Hola, vengo del anuncio de Transform Trauma México 2027. El sitio no me carga bien. ¿Me pueden ayudar a conseguir mi entrada?'
WA = 'https://wa.me/%s?text=%s' % (WA_NUMBER, urllib.parse.quote(WA_MSG))
SITE = 'https://mexico.mastersevents.com'
META_PIXEL_ID = '1640052390439143'  # same pixel as mexico.mastersevents.com so events land in one ad account

logo = read('assets/ttm-2027-logo.svg').strip()
logo = re.sub(r'\s+id="[^"]*"', '', logo).replace('<svg ', '<svg role="img" aria-label="Transform Trauma México 2027" ', 1)
photo = 'data:image/webp;base64,' + base64.b64encode(open(os.path.join(HERE, 'assets/speakers.webp'), 'rb').read()).decode()

CSS = """
@font-face{font-family:PJS;src:url(FONTPATH) format("woff2");font-weight:200 800;font-display:swap}
:root{--m:#5E1737;--pink:#ED21CB;--pink2:#F8B6FA;--green:#477B00;--lime:#B5FA03;--ink:#111;--text:#323232;--mut:#56524E;--paper:#F8F8F8;--wa:#25D366}
*{box-sizing:border-box}
body{margin:0;font:17px/1.55 PJS,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--text);background:#fff}
img,svg{display:block;max-width:100%}
h1,h2,h3{color:var(--ink);line-height:1.15;margin:0 0 .5em;letter-spacing:-.01em}
h1{font-size:clamp(2rem,6vw,3.3rem)}h2{font-size:clamp(1.6rem,4vw,2.3rem)}h3{font-size:1.2rem}
p{margin:0 0 1em}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
.btn{display:inline-block;font-weight:700;text-transform:uppercase;letter-spacing:.02em;text-decoration:none;border-radius:99px;padding:15px 32px;font-size:1rem;line-height:1.3;border:2px solid transparent;text-align:center}
.pk{background:var(--pink);color:#fff;border-color:var(--pink)}.pk:hover{background:#c716aa;border-color:#c716aa}
.gr{background:var(--green);color:#fff;border-color:var(--green)}.gr:hover{background:transparent;color:var(--green)}
.ol{background:transparent;color:var(--ink);border-color:var(--ink)}.ol:hover{background:rgba(0,0,0,.08)}
.bl{display:block;width:100%}
.wa{display:inline-block;background:var(--wa);color:#fff;text-decoration:none;font-weight:700;border-radius:99px;padding:12px 22px;text-align:center}
.wa:hover{background:#128C4A}
header{background:var(--m);color:#fff}
.nav{display:flex;align-items:center;justify-content:space-between;padding:26px 20px;gap:16px}
.nav .logo{width:150px;fill:#fff}
.nav .r{display:flex;align-items:center;gap:18px}
.nav .nl{color:#fff;text-decoration:none;font-weight:700;font-size:.9rem}
.nav .lang{display:flex;gap:8px;font-size:.85rem;font-weight:700}
.nav .lang a{text-decoration:none;color:#fff;padding:6px 10px;border-radius:99px;border:1px solid rgba(255,255,255,.4)}
.nav .lang a.on{background:#fff;color:var(--m)}
.hero{background:var(--m);color:#fff;position:relative;overflow:hidden;padding:24px 0 56px}
.hero:before,.hero:after{content:"";position:absolute;width:520px;height:520px;border:44px solid rgba(255,255,255,.07);border-radius:60px;transform:rotate(30deg);pointer-events:none}
.hero:before{top:-300px;left:-260px}.hero:after{bottom:-320px;right:-240px;border-color:rgba(237,33,203,.22)}
.hero .wrap{position:relative;z-index:1}
.hero h1{color:#fff;max-width:16ch}
.theme{font-size:clamp(1.15rem,2.6vw,1.5rem);font-weight:500;color:var(--pink2);max-width:38ch;margin-bottom:22px}
.intro{max-width:60ch;font-size:1.05rem;margin-bottom:20px}
.meta{font-weight:600;font-size:1.02rem;margin-bottom:30px}
.badge{display:inline-block;background:var(--lime);color:var(--ink);font-weight:700;font-size:.85rem;border-radius:99px;padding:8px 16px;margin-bottom:18px;text-transform:uppercase;letter-spacing:.04em}
.cta{max-width:480px}
.cta .btn{font-size:1.1rem;padding:18px 28px}
.help{margin-top:18px;padding:16px 18px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);border-radius:14px;font-size:.98rem}
.help p{margin:0 0 10px}
section{padding:56px 0}
.alt{background:var(--paper)}
.eyebrow{display:inline-block;font-size:.8rem;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:var(--pink);margin-bottom:10px}
.sp{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
.sp img{border-radius:16px;width:100%;height:auto;box-shadow:0 12px 40px rgba(0,0,0,.14)}
.names{font-weight:600;color:var(--ink)}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:22px;margin-top:28px}
.tile{background:#fff;border-radius:12px;padding:24px 22px;border:1px solid #eee}
.tile b{display:block;font-size:2rem;color:var(--m);line-height:1;margin-bottom:10px}
.tile h3{font-size:1.05rem;margin-bottom:6px}.tile p{font-size:.95rem;color:var(--mut);margin:0}
.tix{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:28px}
.card{background:#fff;border-radius:16px;padding:30px 28px;border:1px solid #eee;display:flex;flex-direction:column}
.card.f{border:2px solid var(--pink)}
.tag{font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--pink)}
.card h3{font-size:1.5rem;margin:6px 0 2px}
.usd,.note{font-size:.85rem;color:var(--mut)}
.price{display:flex;align-items:baseline;gap:12px;margin:14px 0 14px}
.price i{font-style:normal;font-size:.9rem;color:var(--mut)}
.price b{font-size:2.6rem;color:var(--ink);line-height:1}
.price s{font-size:1.1rem;color:var(--mut)}
.card ul{list-style:none;padding:0;margin:8px 0 26px;flex:1}
.card li{position:relative;padding-left:26px;margin-bottom:10px;font-size:.96rem}
.card li:before{content:"";position:absolute;left:0;top:7px;width:14px;height:14px;border-radius:50%;background:var(--lime);box-shadow:inset 0 0 0 3px var(--green)}
.dark{background:var(--m);color:#fff}
.dark h2,.dark h3{color:#fff}
.dark .ol{color:#fff;border-color:#fff}.dark .ol:hover{background:rgba(255,255,255,.12)}
.two{display:grid;grid-template-columns:1.4fr 1fr;gap:32px;align-items:center}
.acts{display:flex;flex-direction:column;gap:12px}
.acts.row{flex-direction:row;flex-wrap:wrap;margin-top:28px}
.elig{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:24px}
.box{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);border-radius:14px;padding:22px}
.box h3{font-size:1.1rem;margin-bottom:8px}.box ul{margin:8px 0 0;padding-left:20px;font-size:.95rem}
footer{background:var(--ink);color:#bbb;font-size:.85rem;padding:40px 0;line-height:1.7}
footer a{color:#ddd;text-decoration:none;margin-right:16px}footer a:hover{color:#fff}
footer .row{display:flex;flex-wrap:wrap;justify-content:space-between;gap:12px 24px;margin-bottom:16px}
footer strong{color:#fff;font-weight:700}
@media(max-width:840px){.sp,.tix,.two,.elig{grid-template-columns:1fr}.sp img{order:-1}}
@media(max-width:520px){body{font-size:16px}section{padding:44px 0}.hero{padding:28px 0 44px}.nav{padding:18px 20px}.nav .nl{display:none}.nav .logo{width:120px}.cta .btn{display:block;width:100%}.price b{font-size:2.2rem}.acts.row a{flex:1 1 100%}}
"""

def page(p):
    wa_btn = '<a class="wa" href="%s" target="_blank" rel="noopener">Escríbenos por WhatsApp</a>' % WA
    tiles = ''.join('<div class="tile"><b>%s</b><h3>%s</h3><p>%s</p></div>' % t for t in p['tiles'])
    def card(c):
        return ('<div class="card%s"><span class="tag">%s</span><h3>%s</h3><span class="usd">%s</span>'
                '<div class="price"><i>Desde</i><b>%s</b><s>%s</s></div>%s<ul>%s</ul>'
                '<a class="btn %s bl" href="%s" data-out data-buy>Comprar entradas</a></div>') % (
            ' f' if c['featured'] else '', c['tag'], c['title'], c['usd'], c['now'], c['was'],
            '<span class="note">%s</span>' % c['note'] if c.get('note') else '',
            ''.join('<li>%s</li>' % li for li in c['items']), 'pk' if c['featured'] else 'gr', p['buy'])
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}">
<meta name="robots" content="noindex,follow">
<link rel="canonical" href="{p['canonical']}">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['desc']}">
<meta property="og:image" content="{SITE}/wp-content/uploads/2026/05/featured-image-new.jpg">
<link rel="icon" href="data:,">
<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','{META_PIXEL_ID}');fbq('track','PageView');</script>
<noscript><img height="1" width="1" style="display:none" alt="" src="https://www.facebook.com/tr?id={META_PIXEL_ID}&ev=PageView&noscript=1"></noscript>
<link rel="preload" href="{p['font']}" as="font" type="font/woff2" crossorigin>
<style>{CSS.strip().replace('FONTPATH', p['font'])}</style>
</head>
<body>
<header><div class="wrap nav">
  <a class="logo" href="{p['home']}" data-out>{logo}</a>
  <div class="r"><a class="nl" href="{p['navlink'][1]}" data-out>{p['navlink'][0]}</a>
  <nav class="lang"><a class="on" href="{p['es']}">ES</a><a href="{p['en']}">EN</a></nav></div>
</div></header>
<main>
<section class="hero"><div class="wrap">
  {p['badge']}<h1>{p['h1']}</h1>
  <p class="theme">Sanación a través de diferentes culturas: espiritualidad, saber y práctica</p>
  {p['intro']}<p class="meta">19-20 de febrero de 2027 · Centro de eventos de Tulum, México, y en línea</p>
  <div class="cta">
    <a class="btn pk bl" href="{p['buy']}" data-out data-buy>{p['buy_label']}</a>
    <div class="help"><p>¿No carga el sitio? Escríbenos por WhatsApp y te ayudamos a conseguir tu entrada.</p>{wa_btn}</div>
  </div>
</div></section>
<section><div class="wrap sp">
  <div><span class="eyebrow">Ponentes</span><h2>Aprende de los expertos líderes que dan forma al futuro del trauma y la sanación</h2>
  <p class="names">{p['names']}</p><p>{p['speakers']}</p>
  <a class="btn ol" href="{SITE}/es/speakers/" data-out>Ver todos los ponentes</a></div>
  <img src="{photo}" width="640" height="461" alt="Ponentes de Transform Trauma México 2027">
</div></section>
<section class="alt"><div class="wrap">
  <span class="eyebrow">Tulum, Riviera Maya</span><h2>Dos días de contenido, toda una vida de práctica.</h2>
  <p style="max-width:70ch">Transform Trauma México, en colaboración con el Newman Institute, reúne a algunas de las voces más influyentes del mundo en el campo de la investigación sobre el trauma, la terapia, la neurociencia y la sanación integrativa, en un extraordinario encuentro de dos días en la Riviera Maya.</p>
  <div class="tiles">{tiles}</div>
</div></section>
<section><div class="wrap">
  <span class="eyebrow">Dos formas de participar</span><h2>{p['tix_h2']}</h2>
  <p style="max-width:70ch">Sé parte de una experiencia impactante y transformadora. Aprende de los principales expertos, adquiere herramientas prácticas que podrás poner en práctica de inmediato y conecta con una comunidad global.</p>
  <div class="tix">{card(p['cards'][0])}{card(p['cards'][1])}</div>
</div></section>
{p['last'](wa_btn)}
</main>
<footer><div class="wrap">
  <div class="row"><strong>Masters Events</strong><span>En colaboración con <strong>Newman Institute</strong></span></div>
  <a href="{SITE}/es/privacy-policy/">Política de privacidad</a><a href="{SITE}/es/terms/">Términos y condiciones</a><a href="https://mastersevents.com/">Ver más eventos</a><br>
  Copyright © 2026 Masters Events Ltd · Registrada en Inglaterra y Gales · Número de empresa: 15061102 · Número de IVA: 448 1305 04
</div></footer>
<script>(function(){{
var q=location.search,l=document.querySelectorAll('a[data-out]'),i;
if(q.length>1)for(i=0;i<l.length;i++)l[i].href+=(l[i].href.indexOf('?')>-1?'&':'?')+q.slice(1);
function t(){{if(window.fbq)fbq.apply(null,arguments)}}
document.addEventListener('click',function(e){{
  var a=e.target.closest&&e.target.closest('a');if(!a)return;
  var d={{page:'{p['page']}',label:(a.textContent||'').trim(),href:a.href}};
  if(a.hasAttribute('data-buy'))t('track','InitiateCheckout',d);
  else if(a.className.indexOf('wa')>-1)t('track','Contact',d);
  else if(a.hasAttribute('data-out'))t('trackCustom','ClickToSite',d);
}});
}})()</script>
</body>
</html>
"""

def home_last(wa_btn):
    return f"""<section class="dark"><div class="wrap two">
  <div><span class="eyebrow">América Latina</span><h2>Fomentando el acceso en toda América Latina</h2>
  <p>Hay un número limitado de becas y descuentos disponibles para participantes de toda América Latina (solo acceso a la conferencia; alojamiento no incluido).</p>
  <p style="margin:0">¿Problemas para abrir el sitio o pagar desde tu país? Escríbenos por WhatsApp y lo resolvemos contigo.</p></div>
  <div class="acts"><a class="btn pk" href="descuento/" data-out>Descuento de Latinoamérica</a><a class="btn ol" href="{SITE}/es/" data-out>Ir al sitio completo</a>{wa_btn}</div>
</div></section>"""

def desc_last(wa_btn):
    return f"""<section class="dark"><div class="wrap">
  <span class="eyebrow">Entradas LATAM</span><h2>Requisitos de elegibilidad</h2>
  <p style="max-width:70ch">Estas entradas con descuento están disponibles únicamente para personas residentes en Latinoamérica. Al comprar, confirmas que resides en un país de Latinoamérica y que la dirección de facturación corresponde a tu lugar de residencia.</p>
  <div class="elig">
    <div class="box"><h3>Entrada presencial</h3><p style="margin:0">Presenta un comprobante de domicilio al registrarte en el evento. La dirección debe coincidir con la de facturación. Sirve uno de estos documentos:</p>
    <ul><li>Pasaporte</li><li>Documento nacional de identidad (INE, DNI, RG, cédula)</li><li>Licencia de conducir</li><li>Factura doméstica reciente o extracto bancario</li></ul></div>
    <div class="box"><h3>Entrada virtual</h3><p style="margin:0">Las entradas virtuales LATAM se emiten de buena fe. Se podrá verificar tu elegibilidad y revocar el acceso si no se puede confirmar tu residencia.</p>
    <p style="margin:16px 0 0">¿Dudas sobre tu elegibilidad o problemas para pagar desde tu país? Escríbenos y lo resolvemos contigo.</p></div>
  </div>
  <div class="acts row"><a class="btn pk" href="{SITE}/es/latam-tickets/" data-out data-buy>Comprar entradas con descuento</a><a class="btn ol" href="{SITE}/es/latam-concession/" data-out>Ir al sitio completo</a>{wa_btn}</div>
</div></section>"""

CE_LI = 'Créditos de desarrollo profesional continuo (CPD) y de educación continua (CE)'
HOME = dict(
    title='Transform Trauma México 2027 · 19-20 de febrero · Tulum y en línea',
    desc='Llega a México la conferencia sobre trauma más grande del mundo. Aprende de Bessel van der Kolk, Dan Siegel, Richard Schwartz y más. 19-20 de febrero de 2027, Tulum y en línea.',
    canonical=SITE + '/es/', page='home', home='./', font='assets/pjs.woff2', navlink=('Descuento de Latinoamérica', 'descuento/'),
    es=SITE + '/es/', en=SITE + '/', badge='',
    h1='Llega a México la conferencia sobre trauma más grande del mundo', intro='',
    buy=SITE + '/es/tickets/', buy_label='Comprar entradas',
    names='Bessel van der Kolk, Dan Siegel, Richard Schwartz y más.',
    speakers='Aprende directamente de líderes reconocidos a nivel mundial, junto con profesionales emergentes y de diversos orígenes culturales, mientras comparten conocimientos de vanguardia, herramientas prácticas y enfoques transformadores. Se anunciarán más ponentes próximamente.',
    tiles=[('2', 'Días de contenido inmersivo', 'Sesiones magistrales, talleres prácticos, debates y oportunidades para conectar.'),
           ('ES · EN', 'Traducción simultánea', 'Todas las sesiones con traducción bilingüe, español e inglés.'),
           ('20', 'Créditos CE / CPD', 'Hasta 20 créditos de Educación Continua y Desarrollo Profesional Continuo.'),
           ('90', 'Días de acceso postconferencia', 'Todas las sesiones disponibles en línea durante 90 días después del evento.')],
    tix_h2='Precio de venta anticipada',
    cards=[dict(featured=True, tag='Presencial', title='Entrada presencial', usd='Todos los precios están en USD', now='$990', was='$1090',
                items=['Acceso a todas las sesiones y paneles en vivo con más de 40 ponentes', 'Traducción simultánea bilingüe (español e inglés)', 'CPD y hasta 20 créditos de Educación Continua (CE)', 'Desayuno, almuerzo y refrescos durante todo el día', 'Acceso a todas las grabaciones durante 90 días', 'Acceso al retiro exclusivo postconferencia en México']),
           dict(featured=False, tag='En línea', title='Entrada virtual', usd='Todos los precios están en USD', now='$225', was='$295',
                items=['Transmisión en vivo de todas las sesiones y paneles con más de 40 ponentes', 'Traducción simultánea bilingüe (español e inglés)', 'CPD y hasta 20 créditos de Educación Continua (CE)', 'Acceso a todas las grabaciones durante 90 días', 'Preguntas y respuestas con los ponentes y chat en vivo, desde computadora o móvil'])],
    last=home_last)
NOTE = 'Con esta entrada no puedes comprar alojamiento en el lugar del evento.'
DESC = dict(
    title='Descuento de Latinoamérica · Transform Trauma México 2027',
    desc='Entradas con descuento exclusivo para residentes de Latinoamérica. Transform Trauma México 2027, 19-20 de febrero, Tulum y en línea. Presencial desde US$495, virtual desde US$95.',
    canonical=SITE + '/es/latam-concession/', page='descuento', home='../', font='../assets/pjs.woff2', navlink=('Inicio', '../'),
    es=SITE + '/es/latam-concession/', en=SITE + '/latam-concession/',
    badge='<span class="badge">Descuento exclusivo para Latinoamérica</span>',
    h1='Llega a México la mayor conferencia del mundo sobre trauma',
    intro='<p class="intro">Contamos con un número limitado de entradas disponibles para profesionales de América Latina, como parte de nuestro compromiso por hacer que este trabajo sea más accesible en diferentes regiones y contextos.</p>',
    buy=SITE + '/es/latam-tickets/', buy_label='Comprar entradas con descuento',
    names='Bessel van der Kolk, Dan Siegel, Dick Schwartz y muchos más.',
    speakers='Transform Trauma México, en colaboración con el Newman Institute, reúne a las voces más influyentes en los campos de la investigación sobre el trauma, la terapia, la neurociencia y la sanación integrativa. Aprende de primera mano de líderes reconocidos a nivel mundial junto con profesionales emergentes y de diferentes culturas. Se anunciarán más ponentes próximamente.',
    tiles=[('2', 'Días de contenido inmersivo', 'Disfruta de un programa variado y dinámico: sesiones magistrales, talleres prácticos, debates y oportunidades para conectar.'),
           ('CPD · CE', 'Desarrollo profesional', 'Se ofrecen créditos de desarrollo profesional continuo (CPD/CE) para apoyar tu aprendizaje y tu crecimiento profesional.'),
           ('90', 'Días de acceso postconferencia', 'Todas las sesiones estarán disponibles en línea durante 90 días después del evento para volver a ver cada sesión e integrar las ideas clave.')],
    tix_h2='Entradas con descuento para Latinoamérica',
    cards=[dict(featured=True, tag='Presencial', title='Entrada presencial', usd='Precio de venta anticipada · USD', now='US$495', was='US$1090', note=NOTE,
                items=['Acceso a todas las sesiones y paneles en vivo con más de 40 ponentes', 'Traducción simultánea bilingüe (español e inglés)', CE_LI, 'Desayuno, almuerzo y refrescos durante todo el día', 'Acceso a todas las grabaciones durante 90 días']),
           dict(featured=False, tag='En línea', title='Entrada virtual', usd='Precio de venta anticipada · USD', now='US$95', was='US$295', note=NOTE,
                items=['Transmisión en vivo de todas las sesiones y paneles con más de 40 ponentes', 'Traducción simultánea bilingüe (español e inglés)', CE_LI, 'Acceso a todas las grabaciones durante 90 días', 'Preguntas y respuestas con los ponentes y chat en vivo, desde computadora o móvil'])],
    last=desc_last)

if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'descuento'), exist_ok=True)
    for out, p in (('index.html', HOME), ('descuento/index.html', DESC)):
        html = page(p)
        open(os.path.join(HERE, out), 'w', encoding='utf-8').write(html)
        print(out, len(html.encode()), 'bytes')
