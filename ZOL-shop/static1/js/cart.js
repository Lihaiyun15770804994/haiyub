$(document).ready(function(){
	//显示隐藏
	$(".site-about .rss").mouseenter(function(){
		$(".rss-layer").show();
	});
	$(".site-about .rss").mouseout(function(){
		$(".rss-layer").hide();
	});
	$(".rss-layer").mouseover(function(){
		$(".rss-layer").show();
	});
	$(".rss-layer").mouseout(function(){
		$(".rss-layer").hide();
	});
	//邮箱验证
	$(".search-sub").click(function(){
		if($(".search-txt").val() == ""){
			$("#tuan-recommend").html("邮箱不能为空！")
			return false;
		};
		var _text = $(".search-txt").val();
		if(!_text.match(/^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/)){
	  	$("#tuan-recommend").html("格式不正确，请重新输入")
	  }else{
	  	$("#tuan-recommend").html("邮箱输入正确！")
	  };
	});
	//页面跳转
	$(".userAbout .loginNow").click(function(){
		location.href = "login.html";
	});
	$(".userAbout .registerNow").click(function(){
		location.href = "register.html";
	});
	//待修改
	
	$("._link .prepage").click(function(){
		location.href = "proPage.html";
	});
	// 读取cookie
	// var goodsList = $.cookie("pro");
	// if(goodsList){
	// 	goodsList = JSON.parse(goodsList);
	// 	for(var i = 0;i<goodsList.length;i++){
	// 		var goods = goodsList[i];
	// 		//创建节点
	// 		var tr = $("<tr class='current'></tr>");
	// 		var td1 = $("<td class='goods'></td>");
	// 		var td2 = $("<td class='unit-price'>" + goods.price + "</td>")
	// 		var td3 = $("<td class='suitId'>" + goods.num + "</td>");
	// 		var td4 = $("<td class='total'>" + goods.totalprice + "</td>");
	// 		var td5 = $("<td class='inventory'>" + goods.store + "</td>");
	// 		var img = $("<img >");
	// 		img.attr("src",goods.src);
	// 		var h3 = $("<h3 class='title'>" + goods.text + "</h3>")
	// 		td1.append(img,h3);
	// 		tr.append(td1,td2,td3,td4,td5);
	// 		tr.appendTo($("table"));
	// 	}
	// 	$("._link .caculate").click(function(){
	// 	$(".current").hide();
	// 	alert("购物车暂时没有商品，去买买买把！");
	// 	window.location.href = "mainPage.html";
	// 	$.cookie("pro", "", {expires:-1, path:"/"});
	// })
	// }
})