var like = document.getElementById('like'),
		dislike = document.getElementById('dislike');

like.addEventListener('click',function(e){
	like.classList.toggle('heart');
	document.getElementsByClassName('heartAnim')[0].classList.toggle('spreadHeart');
});
dislike.addEventListener('click',function(e){
	dislike.classList.toggle('brokeheart');
});