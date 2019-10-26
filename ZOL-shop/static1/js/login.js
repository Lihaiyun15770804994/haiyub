$(document).ready(function(){
	//得到焦点样式
	$(".login_content .userName,.login_content .psd").click(function(){
		$(this).css("border-color","red").siblings().css("border-color","#ccc");
	});
	//跳转页面
	$(".register_bar a").click(function(){
		location.href = "register.html";
	});
	//登录
	//判断是否存在该用户(匹配用户名和密码是否都一致)
	$(".logining").click(function(){
		var users = $.cookie("users");
		if(users){
			users = JSON.parse(users); //cookie中的所有注册过的用户
			var isExists = false; //表示是否存在该用户
			for (var i=0; i<users.length; i++){
				if (users[i].name == $(".txt").val() && users[i].pwd == $(".pwd").val()){
					alert("登录成功");
					console.log( $.cookie("users"));
					location.href = "mainPage.html";
					isExists = true;
				}
			};
			if (!isExists) {
							alert("用户名或密码错误, 请重新输入!");
					}
		}else{
			alert("不存在用户, 请先注册!")
		}
	});
})