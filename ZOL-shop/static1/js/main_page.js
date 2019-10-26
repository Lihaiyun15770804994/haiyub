//头部显示隐藏
$(document).ready(function(){
	$(".quick_menu .attention").mouseover(function(){
		$(".hover_box").show();
	});
	$(".quick_menu .attention").mouseout(function(){
		$(".hover_box").hide();
	});
	$(".quick_menu .hover_box").mouseover(function(){
		$(".quick_menu .hover_box").show();
	});
	$(".quick_menu .hover_box").mouseout(function(){
		$(".quick_menu .hover_box").hide();
	});
	$(".quick_menu .coment").mouseover(function(){
		$(".email_box").show();
	});
	$(".quick_menu .coment").mouseout(function(){
		$(".email_box").hide();
	});
	$(".email_box").mouseover(function(){
		$(".email_box").show();
	});
	$(".email_box").mouseout(function(){
		$(".email_box").hide();
	});
//邮箱验证
	$(".btn").click(function(){
		if($(".txt").val() == ""){
			$(".remind2").html("邮箱不能为空！")
			return false;
		};
		var _text = $(".txt").val();
		if(!_text.match(/^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/)){
	  	$(".remind2").html("格式不正确，请重新输入")
	  }else{
	  	$(".remind2").html("邮箱输入正确！")
	  };
	})
//邮箱验证结束
//头部js结束
//吸顶效果开始
	var _todayTop = $(".today_buy").offset().top;
	$(window).scroll(function(){
		var _scrollTop = $(document).scrollTop();
		if(_scrollTop >= _todayTop){
			$(".today_buy").css({"position":"fixed",top:0,left:95})
		}else{
			$(".today_buy").css("position","static");
		}
	})
	var navTop = $(".suction_tip").offset().top;
	$(window).scroll(function(){
		var _scrollTop = $(document).scrollTop();
		if(_scrollTop >= navTop){
			$(".suction_tip").css({"position":"fixed",top:"45px",left:95})
		}else{
			$(".suction_tip").css("position","static");
		}
	})
	//吸顶效果结束
	//点击回到顶部
	//初始化隐藏内容
	$(".levitate").hide();
	$(window).scroll(function(){
		if($(document).scrollTop() >= 700){
			$(".levitate").fadeIn(1000);
		}else{
			$(".levitate").fadeOut(1000);
		};
	});
	$(".levitate .service").mouseover(function(){
		$(".code-pic").show();
	});
	$(".levitate .service").mouseout(function(){
		$(".code-pic").hide();
	});
	$(".code-pic").mouseover(function(){
		$(".code-pic").show();
	});
	$(".code-pic").mouseout(function(){
		$(".code-pic").hide();
	});
	$(".levitate .goTop").click(function(){
		$('body,html').animate({scrollTop:0},1000);
	})
//轮播图开始
	$.get("josn/lb_content.json", function(data){
						for (var i=0; i<data.length; i++) {
							var obj = data[i]; 
							var li = $("<li></li>");
							var img = $("<img>");
							img.attr("src",obj.name)
							li.append(img);
							$("#list").append(li);
						};
			})
	var _list1 = $("#list");
				var _list2 = $("#list2");
				var _li1 = $("#list li");
				var _li2 = $("#list2 li");
				var size = 4;	
				//显示的图片下标
				var i = 0;
				//启动定时器, 开始自动轮播
				var timer = setInterval(function(){
					i++;
					move();
				}, 2000);
				
				//move,移动
				function move() {
					if (i < 0) {
						_list1.css("left", -(size-1)*700);
						i = size-1; 
					}
					if (i >= size ) {
						_list1.css("left", 0);
						i = 1;
					}
					_list1.stop().animate({left: -i*700},500);
					//按钮的选中状态改变
					_li2.eq(i).removeClass().addClass("active").siblings().removeClass("active")
					if (i == size-1) {
						_li2.eq(0).removeClass().addClass("active").siblings().removeClass("active")
					}
				}
				//上一页
				$("#left").click(function(){
					i--;
					move();
				})
				//下一页
				$("#right").click(function(){
					i++;
					move();
				})
				//按钮的移入事件
				_li2.mouseenter(function(){
					var index = $(this).index();
					i = index;
					move();
				})
				$(".lb_content").hover(function(){ 
					//移入 mouseenter
					clearInterval(timer); //停止定时器, 停止自动轮播
				}, 
				function(){
					//移出, mouseleave
					clearInterval(timer); 
					timer = setInterval(function(){
						i++;
						move();
					}, 2000);
				});
				//轮播图结束
				//产品内容样式开始
				$.get("josn/product.json",function(data){
					for(var i = 0;i<data.length;i++){
						var obj = data[i];
						var li = $("<li><img src=" + obj.src + "><h4>" + obj.name + "</h4><span class='msg'> "+ obj.abstract +" </span><div class='priceBox'><span class='now_price'>" + obj.price + "</span><span class='old_price'>" +obj.sale + "</span><span class='discount_fl'>" + obj.zhehou + "</span><span class='rob'>" + obj.buy + "</span></div></li>");
						$(".product").append(li);
					};
					$(".main_product .product li").click(function(){
						location.href = "proPage.html";
					})
				});	
				//商品详情页跳转
				//产品内容样式结束
				//登录页面跳转
				$(".quick_menu li .login").click(function(){
					location.href = "login.html";
				});
				//注册
				$(".quick_menu li .regisetr").click(function(){
					location.href = "register.html";
				});
})