let infoWarningBtn = $(".info-messages .info-messages-container .info-warning-btn");
let infoWarningBanner = $(".info-messages");

infoWarningBtn.click(() => {
    infoWarningBanner.hide()
});


setTimeout(() => {
    infoWarningBanner.hide()
},5000)