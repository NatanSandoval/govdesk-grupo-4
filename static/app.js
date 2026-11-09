const toggle=document.querySelector('[data-menu-toggle]');
const sidebar=document.querySelector('.sidebar');
const overlay=document.querySelector('.menu-overlay');
function setMenu(open){sidebar?.classList.toggle('is-open',open);overlay?.classList.toggle('is-open',open);toggle?.setAttribute('aria-expanded',String(open));if(open)sidebar?.querySelector('a')?.focus();}
toggle?.addEventListener('click',()=>setMenu(toggle.getAttribute('aria-expanded')!=='true'));
overlay?.addEventListener('click',()=>{setMenu(false);toggle?.focus();});
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&toggle?.getAttribute('aria-expanded')==='true'){setMenu(false);toggle.focus();}});
