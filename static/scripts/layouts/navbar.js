let nav_btn = document.querySelector(".nav-bar .nav-container .nav-links .profile-info-img");
let nav_link = document.querySelector(".nav-bar .nav-container .nav-links .nav-links-section")
let nav_open = false;

nav_btn.addEventListener("click", () => {
    if(nav_open === false){
        nav_link.style.display= "flex";
        nav_open = true;

    }
    else if(nav_open === true){
        nav_link.style.display = "none"
        nav_open = false;

    }
})