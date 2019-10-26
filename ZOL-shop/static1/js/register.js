$(document).ready(function(){
	//得到焦点样式
	$(".login_content .userName,.login_content .psd").click(function(){
		$(this).css("border-color","red").siblings().css("border-color","#ccc");
	});
	//登录页面跳转
	$(".register_bar a").click(function(){
		location.href = "login.html";
	});
	//cookie的创建
	var arr = [];
	var obj1 = {};
	obj1.name = "huangshu110";
	obj1.pwd = "1234567";
	arr.push(obj1);
	$.cookie("users", JSON.stringify(arr), {expires:22, path:"/"});
	//如果已经存在该用户, 不能注册
	//不存在则注册, 保存到cookie
	$(".logining").click(function(){
		//获取cookie
		var users = $.cookie("users") ? JSON.parse($.cookie("users")) : [];
		//先判断是否存在该用户
		for(var i = 0;i<users.length;i++){
			if ( users[i].name == $(".txt").val()){
				alert("用户名已存在! 不能注册相同的用户");
				return;
			}else{
				alert("用户名注册成功,，请登录！");
			location.href = "login.html";
				
				}
		}
		//注册新用户
		var user = {
			name:$(".txt").val(),
			pwd:$(".pwd").val(),
		};
		users.push(user);
		$.cookie("users", JSON.stringify(users), {expires:22, path:"/"});
		console.log( $.cookie("users"));
	})
	//获取
	//用户名正则验证
	$(".txt").blur(function(){
		var userName = $(this).val();
		if(userName.length == ""){
			alert("用户名不能为空");
		}
		else if(!/[a-zA-Z0-9]{3,8}/.test(userName)){
			alert("用户名格式错误!");
			return false;
		};
	});
	$(".pwd").blur(function(){
		var passWord = $(this).val();
		if(passWord.length == ""){
			alert("密码不能为空")
		}
		else if(!/^[0-9a-zA-Z_]{6,15}$/.test(passWord)){
			alert("密码长度错误!");
			return false;
		};
	});
})