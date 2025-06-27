// Función para filtrar productos según la categoría seleccionada
function filterProducts(category) {
    const products = document.querySelectorAll('.producto'); // Selecciona todos los productos
    products.forEach(product => {
        // Muestra u oculta productos según la categoría
        if (category === 'todos' || product.classList.contains(category)) {
            product.style.display = 'block';
        } else {
            product.style.display = 'none';
        }
    });
}

  var swiper = new Swiper(".mySwiper", {
    loop: true,
    autoplay: {
      delay: 3000,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });


