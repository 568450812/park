$(function (){
	//1.全选和取消全选
	var isChecked = false;
	$(".checkAll").click(function (){
		isChecked = !isChecked;
		if(isChecked){
			//切换选中样式
			$(this)
				.attr("src","../images/cart/product_true.png");
			$(".checkImg")
				.attr("src","../images/cart/product_true.png")
				.attr("checked","true");//修改状态标记
		}else{
			$(this)
				.attr("src","../images/cart/product_normal.png")
			$(".checkImg")
				.attr("src","../images/cart/product_normal.png")
				.removeAttr("checked");
		}
	})
	//2.反选
	$(".checkImg").click(function (){
		//如果当前元素存在checked属性值，
		//说明原本是选中状态，需要改为取消选中
		if($(this).attr("checked")){
			$(this)
				.attr("src","../images/cart/product_normal.png")
				.removeAttr("checked");
		}else{
			$(this).attr("checked","true")
				.attr("src","../images/cart/product_true.png");

		}
		//反选：被选中的图片数量与列表中图片数量一致，
		//视为全选
		if($("img[checked]").length == $(".checkImg").length){
			$(".checkAll")
				.attr("src","../images/cart/product_true.png");
			//修改全选按钮的状态标记
			isChecked = true;
		}else{
			$(".checkAll")
				.attr("src","../images/cart/product_normal.png");
			//修改全选按钮的状态标记
			isChecked = false;
		}

	})








})