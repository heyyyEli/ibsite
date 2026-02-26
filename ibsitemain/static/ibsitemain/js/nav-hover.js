document.addEventListener('DOMContentLoaded', () => {
  const fluidEffect = document.querySelector('.fluid-hover-effect');
  const nav = document.querySelector('nav');
  let animationFrame;
  let currentX = 0, targetX = 0;
  let currentWidth = 0, targetWidth = 0;

  if (!fluidEffect || !nav) return;

  function animate() {
    // Calculate distance
    const distanceX = Math.abs(targetX - currentX);
    const distanceWidth = Math.abs(targetWidth - currentWidth);
    
    // Dynamic speed - faster overall
    // Minimum speed increased from 0.15 to 0.25
    // Maximum speed increased from 0.4 to 0.6
    // Distance multiplier increased for quicker response
    const speedX = Math.min(0.6, Math.max(0.25, distanceX * 0.005));
    const speedWidth = Math.min(0.6, Math.max(0.25, distanceWidth * 0.005));
    
    // Apply the dynamic speed
    currentX += (targetX - currentX) * speedX;
    currentWidth += (targetWidth - currentWidth) * speedWidth;
    
    fluidEffect.style.transform = `translateY(-50%) translateX(${currentX}px)`;
    fluidEffect.style.width = `${currentWidth}px`;
    animationFrame = requestAnimationFrame(animate);
  }
  animate();

  nav.addEventListener('mousemove', e => {
    const li = e.target.closest('li');
    if (li && nav.contains(li)) {
      const navRect = nav.getBoundingClientRect();
      const rect = li.getBoundingClientRect();
      targetX = rect.left - navRect.left;
      targetWidth = rect.width;
    }
  });

  nav.addEventListener('mouseleave', () => {
    const activeLi = nav.querySelector('li.active');
    if (activeLi) {
      const navRect = nav.getBoundingClientRect();
      const rect = activeLi.getBoundingClientRect();
      targetX = rect.left - navRect.left;
      targetWidth = rect.width;
    } else {
      targetWidth = 0;  // hide highlight
    }
  });
});