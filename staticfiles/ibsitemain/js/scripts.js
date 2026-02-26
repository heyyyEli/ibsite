document.addEventListener('DOMContentLoaded', () => {
  // Create modal container and append to body
  const modal = document.createElement('div');
  modal.classList.add('modal');
  modal.setAttribute('aria-hidden', 'true');

  modal.innerHTML = `
    <div class="modal__backdrop" data-close></div>
    <div class="modal__panel" role="document" aria-labelledby="modal-title" tabindex="0">
      <div class="modal__header">
        <h2 class="modal__title" id="modal-title">Modal Title</h2>
        <button class="modal__close" type="button" aria-label="Close">&times;</button>
      </div>
      <div class="modal__content" id="modal-content">Your modal content goes here.</div>
    </div>
  `;

  document.body.appendChild(modal);

  // Open modal with custom content and title
  function openModal(content = '', title = 'Details') {
    document.getElementById('modal-title').textContent = title;
    document.getElementById('modal-content').innerHTML = content;
    modal.setAttribute('aria-hidden', 'false');
    modal.classList.add('open');
    modal.querySelector('.modal__panel').focus();
    // prevent background scroll
    document.body.classList.add('modal-open');
  }

  // Close the modal
  function closeModal() {
    modal.setAttribute('aria-hidden', 'true');
    modal.classList.remove('open');
    // restore background scroll
    document.body.classList.remove('modal-open');
  }

  // Close modal on backdrop click or close button
  modal.addEventListener('click', e => {
    if (e.target.hasAttribute('data-close') || e.target.classList.contains('modal__close')) {
      closeModal();
    }
  });

  // Close on Escape key
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && modal.classList.contains('open')) {
      closeModal();
    }
  });

  // Public methods
  window.openModal = openModal;
  window.closeModal = closeModal;

  // Modal triggers: elements with data-open-modal attribute
  const triggers = document.querySelectorAll('[data-open-modal]');
  triggers.forEach(button => {
    button.addEventListener('click', () => {
      const contentId = button.getAttribute('data-modal-target');
      const title = button.getAttribute('data-modal-title') || 'Details';
      const contentTemplate = document.querySelector(contentId);
      if (contentTemplate) {
        openModal(contentTemplate.innerHTML, title);
      }
    });
  });
});




function showTab(tab) {
  const benefitsSection = document.getElementById('benefits-section');
  const disadvantagesSection = document.getElementById('disadvantages-section');
  const benefitsTab = document.querySelector('li a[href="#benefits"]').parentElement;
  const disadvantagesTab = document.querySelector('li a[href="#disadvantages"]').parentElement;

  if (tab === 'benefits') {
    benefitsSection.style.display = '';
    disadvantagesSection.style.display = 'none';
    benefitsTab.classList.add('active');
    disadvantagesTab.classList.remove('active');
  } else {
    benefitsSection.style.display = 'none';
    disadvantagesSection.style.display = '';
    disadvantagesTab.classList.add('active');
    benefitsTab.classList.remove('active');
  }
}

window.onload = function() {
  // Set initial visibility based on active_tab context variable
  const activeTab = "{{ active_tab }}";  // This is injected by Django template rendering
  showTab(activeTab);
};
