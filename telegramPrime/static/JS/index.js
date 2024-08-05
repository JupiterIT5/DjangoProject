console.log('made by "Fcore" :)');
const changeBackground = () => {
  const headerBackground = document.querySelector(".header__background");
  const choosen = document.querySelector(".choosen");
  const headerLogo = document.querySelector(".header__logo");
  const headerContact = document.querySelector(".header__contact");

  if (window.pageYOffset == 0) {
    headerBackground.classList.remove("show__header");
    headerLogo.classList.remove("show__header__v2");
    headerContact.classList.remove("show__header__v2");
    choosen.style.color = "#1c9ee0";
  } else {
    headerBackground.classList.add("show__header");
    headerLogo.classList.add("show__header__v2");
    headerContact.classList.add("show__header__v2");
    choosen.style.color = "#a6d9f3";
  }
};
changeBackground();

const scrollToBlock = (px) => window.scrollTo({ top: px, behavior: "smooth" });

const showShopCategory = (id) => {
  const categories = document.querySelectorAll(".nav__list");
  const shopSections = document.querySelectorAll(".shop__section");

  shopSections.forEach((section) => {
    section.classList.remove("showed__section");
    categories.forEach((category) => {
      category.classList.remove("choosen__category");
    });
  });
  shopSections[id].classList.add("showed__section");
  categories[id].classList.add("choosen__category");
};

// counter

function counterUp(el, t) {
  let n = 0;
  const r = parseFloat(el.innerHTML);
  const finalValue = Number.isInteger(r) ? parseInt(r, 10) : r;
  const i = t.duration || 2000;
  const u = t.delay || 16;
  const step = finalValue / (i / u);

  const l = setInterval(() => {
    n += step;
    el.innerHTML = Number.isInteger(finalValue) ? Math.floor(n) : n.toFixed(2);
    if (n >= finalValue) {
      clearInterval(l);
      el.innerHTML = finalValue;
    }
  }, u);
}

const counterElements = document.querySelectorAll(".counter");
counterElements.forEach((el) => {
  const IO = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        counterUp(entry.target, { duration: 2000, delay: 16 });
        IO.unobserve(entry.target); // Stop observing once the element is intersecting
      }
    });
  });
  IO.observe(el);
});

const showHideBurger = (state) => {
  const burger = document.querySelector(".burger__menu");
  if (state == 0) {
    burger.classList.remove("hide__burger");
  } else {
    burger.classList.add("hide__burger");
  }
};
// swipers
const swiperLogo = new Swiper(".logo-container", {
  spaceBetween: 40,
  speed: 6000,
  loop: true,
  leftToRight: true,
  autoplay: {
    delay: 1,
  },
  breakpoints: {
    320: {
      slidesPerView: 1,
    },

    750: {
      slidesPerView: 1.8,
    },
    1200: {
      slidesPerView: 2,
    },

    1500: {
      slidesPerView: 2.3,
    },
  },
});

const swiperScreenshots = new Swiper(".screenshot-container", {
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  spaceBetween: 100,
  centeredSlides: true,
  initialSlide: 1,
  loop: true,
});

const clients = new Swiper(".reviews-container", {
  spaceBetween: 30,
  speed: 2500,
  loop: true,
  leftToRight: true,
  centeredSlides: true,

  autoplay: {
    delay: 2500,
  },
  breakpoints: {
    320: {
      slidesPerView: 1,
    },

    768: {
      slidesPerView: 2,
    },
    1200: {
      slidesPerView: 3,
    },
  },
});

const partners = new Swiper(".partner-container", {
  spaceBetween: 24,
  speed: 6000,
  loop: true,
  leftToRight: true,
  autoplay: true,
  autoplayDisableOnInteraction: false,
  breakpoints: {
    320: {
      slidesPerView: 2,
    },
    576: {
      slidesPerView: 3,
    },
    768: {
      slidesPerView: 4,
    },
    1200: {
      slidesPerView: 5,
    },
    1400: {
      slidesPerView: 6,
    },
  },
});

function toggleTheme() {
  const page = document.querySelector(".page");
  if (page.classList.contains("light")) {
    page.classList.remove("light");
    page.classList.add("dark");
  } else {
    page.classList.remove("dark");
    page.classList.add("light");
  }
}

function toggleLanguage() {
  const translateWords = document.querySelectorAll(".translate");
  const lang = document.querySelector(".lang__text");
  const langImage = document.querySelector(".lang__img");
  if (lang.innerHTML === "RU") {
    translateWords.forEach((el, i) => {
      el.innerHTML = languages.en[i];
    });
    lang.innerHTML = "EN";
    langImage.src = "./IMG/en.webp";
  } else if (lang.innerHTML === "EN") {
    translateWords.forEach((el, i) => {
      el.innerHTML = languages.ru[i];
    });
    lang.innerHTML = "RU";
    langImage.src = "./IMG/ru.webp";
  }
}
const showContacts = (button) => {
  const showContactBlock = document.querySelector(".show__contacts");
  if (button.innerHTML == "Показать контакты") {
    button.innerHTML = "Скрыть контакты";
    showContactBlock.style.display = "block";
    setTimeout(() => {
      showContactBlock.classList.add("show");
    }, 1);
  } else {
    button.innerHTML = "Показать контакты";
    showContactBlock.classList.remove("show");
    setTimeout(() => {
      showContactBlock.style.display = "none";
    }, 1000);
  }
};

let currentOpenIndex = null;

const showKnowledgeBase = (index) => {
  const showKnowBase = document.querySelectorAll(".know__answers");
  const showKnowText = document.querySelectorAll(".know__list");
  if (currentOpenIndex !== null) {
    showKnowBase[currentOpenIndex].classList.remove("show__base");
    showKnowText[currentOpenIndex].classList.remove("show__text");
  }
  showKnowBase[index].classList.add("show__base");
  showKnowText[index].classList.add("show__text");
  currentOpenIndex = index;
};

let currentOpenIndexSec = null;
const showAnswerQuestion = (index) => {
  const showAnswersBlock = document.querySelectorAll(".answer");
  const answerText = document.querySelectorAll(".answer__text")
  if (currentOpenIndexSec !== null) {
    showAnswersBlock[currentOpenIndexSec].classList.remove("show__answer");
    answerText[currentOpenIndexSec].classList.remove("show__text");
  }
  showAnswersBlock[index].classList.add("show__answer");
  answerText[index].classList.add("show__text");
  currentOpenIndexSec = index;
};


// let useSecondState = false;
// const showAnswerQuestion = (state) => {
//   const showAnswersBlock = document.querySelectorAll(".answer");
//   const answerText = document.querySelectorAll(".answer__text")
//   for (let i = 0; i < showAnswersBlock.length; i++) {
//     if (state == i && useSecondState == false) {
//       useSecondState = true;
//       showAnswersBlock[i].classList.add("show__answer");
//       answerText[i].classList.add("show__text")
//     } else if (state == i && useSecondState == true) {
//       useSecondState = false;
//       showAnswersBlock[i].classList.remove("show__answer");
//       answerText[i].classList.remove("show__text")
//     }
//   }
// };
