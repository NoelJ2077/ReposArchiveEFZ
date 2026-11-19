let countdown = 15;

function updateTicker() {
    fetch('/random_ticker')
        .then(response => response.json())
        .then(data => {
            document.getElementById('ticker').innerText = data.ticker;
            document.getElementById('price').innerText = data.price;
            countdown = 15; // Reset countdown
        })
        .catch(error => console.error('Error fetching ticker:', error));
}

setInterval(() => {
    if (countdown > 0) {
        countdown--;
        document.getElementById('countdown').innerText = countdown;
    } else {
        updateTicker();
    }
}, 1000); // Update countdown every second

// Initial ticker fetch
updateTicker();

fetch('/get_emailJS_pub_key')
.then(response => response.json())
.then(data => {
  emailjs.init(data.key);
})
.catch(error => console.error('Error fetching emailJS public key:', error));


var lastSentTime = localStorage.getItem('lastSentTime') ? parseInt(localStorage.getItem('lastSentTime')) : 0;

// for hovering over * data
(function () {
$('[data-toggle="tooltip"]').tooltip();
});

function sendMail() {
var currentTime = new Date().getTime();
if (currentTime - lastSentTime < 3 * 60 * 1000) {
    alert('Please wait at least 3 minutes before sending another message.');
    return;
}
var frommail = document.getElementById('frommail').value;
var fromname = document.getElementById('fromname').value;
var subject = document.getElementById('subject').value;
var message = document.getElementById('message').value;

// Parameter names must match EmailJS template parameters
var templateParams = {
    fromemail: frommail,
    fromname: fromname,
    subject: subject,
    message: message
};

// Send email via EmailJS
emailjs.send('service_utqf0dw_secret_0', 'template_pb0y8ab_secret0', templateParams)
    .then(function(response) {
        console.log('SUCCESS!', response.status, response.text);
        alert('Message sent successfully!');
        // Update lastSentTime in localStorage
        lastSentTime = currentTime;
        localStorage.setItem('lastSentTime', lastSentTime);
    }, function(error) {
        console.log('FAILED...', error);
        alert('Message failed to send. Please try again later.');
    });
}
// trigger ticker update manually
document.getElementById('tickercss').addEventListener('click', function() {
    fetch('/random_ticker')
        .then(response => response.json())
        .then(data => {
            document.getElementById('ticker').innerText = data.ticker;
            document.getElementById('price').innerText = data.price;
            countdown = 15; // Reset countdown if applicable
        })
        .catch(error => console.error('Error fetching ticker:', error));
});
document.addEventListener('DOMContentLoaded', function () {
    // Alle Navigationslinks erfassen
    const navLinks = document.querySelectorAll('nav a[js-title]');

    // Event Listener für Klicks auf Navigationslinks hinzufügen
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            document.title = this.getAttribute('js-title');
        });
    });

    // Alle Sektionen erfassen
    const sections = document.querySelectorAll('section');
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.5
    };

    // IntersectionObserver für das Scrollen einrichten
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const sectionId = entry.target.id;
                const link = document.querySelector(`nav a[href="#${sectionId}"]`);
                if (link) {
                    document.title = link.getAttribute('js-title');
                }
            }
        });
    }, observerOptions);

    // Observer für jede Sektion hinzufügen
    sections.forEach(section => {
        observer.observe(section);
    });
});
