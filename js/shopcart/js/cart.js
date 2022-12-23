$(function() {
	// 1全选，全不选
	// 把全选按钮（checkall）的状态赋值给三个小的按钮（j-checkbox）
	$(".checkall").change(function() {
		// console.log($(this).prop("checked"));
		// $(".j-checkbox").prop("checked",true);
		$(".j-checkbox,.checkall").prop("checked", $(this).prop("checked"));
		getSum();
	})
	// 如果小复选框被选中的个数等于3，则全选被选上，否则全选不选
	$(".j-checkbox").change(function() {
		// if(选中的小复选框的个数===3){
		// 	全选选中
		// }else{
		// 	全选不选
		// }
		// console.log($(".j-checkbox:checked"));
		// console.log($(".j-checkbox:checked").length);
		// if($(".j-checkbox:checked").length===3){
		if ($(".j-checkbox:checked").length === $(".j-checkbox").length) {
			$(".checkall").prop("checked", true);
		} else {
			$(".checkall").prop("checked", false);
		}
		getSum();

	});

	//2增减商品数量
	$(".increment").click(function() {
		// 得到当前兄弟文本框的值
		var n = $(this).siblings(".itxt").val();
		// console.log(n);
		n++;
		$(this).siblings(".itxt").val(n);
		// 3计算小计模块 文本框的值*当前商品价格
		// 当前商品价格 p
		// var p=$(this).parent().parent().siblings(".p-price").html();
		// parents(".p-num")返回指定的祖先元素
		var p = $(this).parents(".p-num").siblings(".p-price").html();
		// console.log(p);
		p = p.substr(1);//34.00
		console.log(p);
		// 小计
		$(this).parent().parent().siblings(".p-sum").html("￥" + (p * n).toFixed(2));
		getSum();
	})
	$(".decrement").click(function() {
		// 得到当前兄弟文本框的值
		var n = $(this).siblings(".itxt").val();
		if (n == 1) {
			return false;
		}
		n--;
		$(this).siblings(".itxt").val(n);
		// 当前商品价格 p
		var p = $(this).parent().parent().siblings(".p-price").html();
		// console.log(p);
		p = p.substr(1);
		console.log(p);
		// 小计
		$(this).parent().parent().siblings(".p-sum").html("￥" + (p * n).toFixed(2));
		getSum();
	});
	// 4文本框发生变化，计算小计
	$(".itxt").change(function() {
		//先获取文本框的值
		var n = $(this).val();
		// 当前商品价格 p
		var p = $(this).parent().parent().siblings(".p-price").html();
		// console.log(p);
		p = p.substr(1);
		console.log(p);
		// 小计
		$(this).parent().parent().siblings(".p-sum").html("￥" + (p * n).toFixed(2));
		getSum();
	})
	// 5总计和总价
	getSum();

	function getSum() {
		var count = 0;
		var money = 0;
		// 总计
		// $(".itxt").each(function(i, ele) {
		// 	count += parseInt($(ele).val());
		// });		
		var item = $(".j-checkbox:checked").parents(".cart-item");
		item.find(".itxt").each(function(i, ele) {
			count += parseInt($(ele).val());
		});
		$(".amount-sum em").text(count);
		// 总价
		// $(".p-sum").each(function(i, ele) {
		// 	money += parseFloat($(ele).text().substr(1));
		// });		
		item.find(".p-sum").each(function(i, ele) {
			money += parseFloat($(ele).text().substr(1));
		});
		$(".price-sum em").text("￥" + money.toFixed(2));
	}
	// 删除商品
	$(".p-action").click(function() {
		$(this).parents(".cart-item").remove();
		getSum();
	});
	// 删除所有复选框选中的商品
	$(".remove-batch").click(function() {
		$(".j-checkbox:checked").parents(".cart-item").remove();
		getSum();
	});
	// 清理购物车
	$(".clear-all").click(function() {
		// $(".cart-item").remove();
		$(".cart-item-list").html("");
		getSum();
	})

})
