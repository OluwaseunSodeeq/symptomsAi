 // Function to get the current year and insert it into the HTML
 function displayCurrentYear() {
  const currentYear = new Date().getFullYear();
  document.getElementById("currentYear").textContent = currentYear;
}

// Menu bar functionlity

document.addEventListener('DOMContentLoaded', function() {
 const hamburgerMenu = document.querySelector('.hamburger-menu');
 const navigation = document.querySelector('.navigation');
 const headerLogo = document.getElementById('header-logo');
 const navLinks = document.querySelectorAll('.navigation a');

 
  hamburgerMenu.addEventListener('click', function() {
      navigation.classList.toggle('show');
      headerLogo.classList.toggle('hide');
  });

  navLinks.forEach(link => {
      link.addEventListener('click', function() {
        navigation.classList.remove('show');
        headerLogo.classList.remove('hide');
      });
  });

});


  
  //Functionality for the login User email check sign 
  document.addEventListener('DOMContentLoaded', function() {
    const emailInput = document.getElementById('email');
    const checkIcon = document.querySelector('.check');

    emailInput.addEventListener('input', function() {
      if (validateEmail(emailInput.value)) {
        checkIcon.style.display = 'block'; // Show the check icon
      } else {
        checkIcon.style.display = 'none'; // Hide the check icon
      }
    });
  });

  function validateEmail(email) {
    const regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return regex.test(email.toLowerCase());
  }

  // When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};
        
function scrollFunction() {
   if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
     document.getElementById("myBtn").style.display = "block";
   } else {
     document.getElementById("myBtn").style.display = "none";
   }
}
 
 // Functionality for back to top button
function topFunction() {
   document.body.scrollTop = 0; // For Safari
   document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE, and Opera
}