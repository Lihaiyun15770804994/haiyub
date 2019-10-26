$(document).ready(function(){
	//显示隐藏
	$(".title").mouseenter(function(){
		$(".rss-layer").show();
	});
	$(".title").mouseout(function(){
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
	  	$("#tuan-recommend").html("格式不正确，请重新输入");
	  }else{
	  	$("#tuan-recommend").html("邮箱输入正确！")
	  };
	});
	//邮箱验证结束
	//页面跳转
	$(".loginNow").click(function(){
		location.href = "login.html";
	});
	$(".registerNow").click(function(){
		location.href = "register.html";
	});
	//跳转到首页
	$(".nav_list li").eq(0).click(function(){
		location.href = "mainPage.html";
	});
	//显示隐藏
	$(".history span").mouseenter(function(){
		$(".-hide").show();
	});
	$(".history span").mouseout(function(){
		$(".-hide").hide();
	});
	$(".-hide").mouseenter(function(){
		$(".-hide").show();
	});
	$(".-hide").mouseout(function(){
		$(".-hide").hide();
	});
	//获取json
// 	$.get("/static1/josn/details.json",function(data){
// 		for(var i = 0;i<data.length;i++){
// 			var obj = data[i];
// //			console.log(obj);
// 			var name = $("<a href='#'>" + obj.name + "</a>");
// 			var span = $("<span>" + obj.title + "<span>");
// 			$(".descript").append(name,span);
// 			//切换图片
// 			var liOne = $("<li></li>");
// 			var img = $("<img>");
// 			img.attr("src",obj.src[0])
// 			liOne.append(img);
// 			var liTwo = $("<li></li>");
// 			var img = $("<img>");
// 			img.attr("src",obj.src[1])
// 			liTwo.append(img);
// 			var liThree = $("<li></li>");
// 			var img = $("<img>");
// 			img.attr("src",obj.src[2])
// 			liThree.append(img);
// 			var liFour = $("<li></li>");
// 			var img = $("<img>");
// 			img.attr("src",obj.src[3])
// 			liFour.append(img);
// 			$(".smallImg").append(liOne,liTwo,liThree,liFour);
// 			//商品详情
// 			var h3 = $("<h3>" + obj.descript + "</h3>");
// 			var p = $("<p>"+ obj.property +"</p>");
// 			var gift = $("<div class='gift'><span>" + obj.gift + "</span></div>");
// 			var div = $("<div class='price'><span class='sellPrice'>" + obj.price + "</span><span class='oldPrice'>" + obj.preprice + "</span><span class='discount'>" + obj.discount + "</span></div>");
// 			var list = $("<ul class='list'><li><em>23</em>人购买</li><li><em>暂无评价</em></li></ul>");
// 			var buyNow = $("<div class='buy'><input type='submit' value='添加到购物车' class='btn'/></div>")
// 			$(".detail").append(h3,p,gift,div,list,buyNow);
// 		};
		//图片切换
// 		$(".smallImg li").mouseenter(function(){
// 			var index = $(this).index();
// 			$(".showImg li").eq(index).show().siblings().hide();
// 		});
// 		//放大镜
// 		var _smallImg = $(".smallImg"); //小图
// 		var _smallArea = $(".focus"); //小区域
// 		var _bigImg = $(".bigImg"); //大图
// 		var _bigArea = $(".bigArea"); //大区域
// 		_smallArea.width( _smallImg.width()/_bigImg.width() * _bigArea.width() );
// 		_smallArea.height( _smallImg.height()/_bigImg.height() * _bigArea.height() );
// 		//放大系数(放大倍数)
// 		var scale = _bigImg.width() / _smallImg.width();
// 		_smallImg.mousemove(function(e){
// 			_smallArea.show();
// 			_bigArea.show();
// 			var x = e.pageX - _smallImg.offset().left - _smallArea.width()/2;
// 			var y = e.pageY - _smallImg.offset().top - _smallArea.height()/2;
// 			if (x < 0) {
// 						x = 0;
// 					}
// 			else if (x > _smallImg.width() - _smallArea.width()) {
// 						x = _smallImg.width() - _smallArea.width();
// 					}
// 			if (y < 0) {
// 						y = 0;
// 					}
// 			else if (y > _smallImg.height() - _smallArea.height()) {
// 						y = _smallImg.height() - _smallArea.height();
// 					}
// 			_smallArea.css({left: x, top: y});
//
// 			//移动大图
// 			_bigImg.css({left: -x*scale, top: -y*scale});
// 		})
// 		_smallImg.mouseleave(function(){
// 					_smallArea.hide(); //隐藏小区域
// 					_bigArea.hide();
// 				})
// 		buyNow.click(function(){
// 			//创建cookie
// 			var arr = [];
// 			var pro1 = {
// 				id :1,
// 				src:"img/huawei.jpg",
// 				text:"曲面黑科技 三星23.5英寸曲面竞技显示器",
// 				price:"￥500.00",
// 				num:1,
// 				totalprice:"￥500.00",
// 				store:"有货"
// 			}
// 			arr.push(pro1);
// 			$.cookie("pro", JSON.stringify(arr), {expires:22, path:"/"});
// //			console.log( $.cookie("pro"));
// 			window.location.href="cart.html"
// 		})
// 	})
})

//content[5].onclick = function(){
//	window.open(proPage.html + '?id=5')
//}
//
//var text = window.search();  //id=5

