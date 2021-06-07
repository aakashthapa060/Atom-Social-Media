// Cover Pic
let cover_pic = document.querySelector(".profile-container .profile-section-main .profile-section .profile-main-part .profile-part-cover-img img");

function cover_change(){
    cover_pic.src = `https://source.unsplash.com/1600x900/?art,nature`;
}
cover_change()



// let follow_unfollow_btn = document.querySelector(".profile-container .profile-section-main .profile-section .profile-main-part .profile-info-part .profile-info-container .follow-unfollow form button");

// follow_unfollow_btn.addEventListener("click", () => {
//     alert("helo")
// })



let change_profile_btn = $(".profile-container .profile-section-main .profile-section .profile-main-part .profile-info-part .profile-info-container .follow-unfollow .profile-change-btn")
let profile_form_close_btn1 = $(".profile-edit .profile-form-container .profile-form-title .profile-form-close-btn")
let profile_form_close_btn2 = $(".profile-edit .profile-form-container .actual-profile-form form .buttons a")
let profile_change_form = $(".profile-edit");

let profile_open = false
change_profile_btn.click(() => {
    if (profile_open === false){
        profile_change_form.css("display", "block")
        profile_open = true
    }
})

profile_form_close_btn1.click(() => {
    if(profile_open === true){
        profile_change_form.css("display", "none");
        profile_open = false
    }
})
profile_form_close_btn2.click(() => {
    if(profile_open === true){
        profile_change_form.css("display", "none");
        profile_open = false
    }
})


//Profile Link Edit
let profile_link_cancle_btn = $(".profile-link-section .profile-link-form .profile-link-container .actual-profile-link-form form .buttons a");
let profile_link_container = $(".profile-link-section ")
let profile_link_btn = $(".profile-container .profile-section-main .profile-section .profile-main-part .profile-info-part .profile-info-container .follow-unfollow .profile-link-btn")
profile_link_open = false

profile_link_btn.click(() => {
    if(profile_link_open === false){
        profile_link_container.fadeIn()
        profile_link_open = true
    }
});

profile_link_cancle_btn.click(() => {
    if(profile_link_open === true){
        profile_link_container.fadeOut()
        profile_link_open = false
    }
})