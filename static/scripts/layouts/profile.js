// Cover Pic
let cover_pic = document.querySelector(".profile-container .profile-section-main .profile-section .profile-main-part .profile-part-cover-img img");

function cover_change(){
    cover_pic.src = `https://source.unsplash.com/1600x900/?art,nature`;
    alert(randomNum)
}
cover_change()



let follow_unfollow_btn = document.querySelector(".profile-container .profile-section-main .profile-section .profile-main-part .profile-info-part .profile-info-container .follow-unfollow form button");

follow_unfollow_btn.addEventListener("click", () => {
    alert("helo")
})
