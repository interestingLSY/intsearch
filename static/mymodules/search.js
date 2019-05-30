String.prototype.replaceAll = function (exp, newStr) {
    return this.replace(new RegExp(exp, "gm"), newStr);
};
/**
by 花果山总钻风
https://blog.csdn.net/dszgf5717/article/details/51314952
 * 原型：字符串格式化
 * @param args 格式化参数值
 */
String.prototype.format = function(args) {
    var result = this;
    if (arguments.length < 1) {
        return result;
    }
    var data = arguments; // 如果模板参数是数组
    if (arguments.length == 1 && typeof (args) == "object") {
        // 如果模板参数是对象
        data = args;
    }
    for ( var key in data) {
        var value = data[key];
        if (undefined != value) {
            result = result.replaceAll("\\{" + key + "\\}", value);
        }
    }
    return result;
}

function Search(q){
	console.log(q);
	var results
	$.getJSON({
		url: "/api/search?q="+q,
		success: function(res){
			results = res
		},
		async: false
	});
	return results
}

function Response(){
	$("#search-box").animate({
		left: '3%',
		top: '6%'
	})

	results = Search($("#q").val())
	console.log(results);

	$("#search-result-box").empty()
	for( var i = 0 ; i < results.length ; ++i ){
		var result = results[i]
		now_html = "\
			<div class=\"search-result\">\n\
				<h1> <a href=\"{link}\"> {title} </a> </h1>\n\
				<p> {description}... </p>\n\
			</div>\n".format({
				title: result.title,
				link: result.link,
				description: result.description
			})
		$("#search-result-box").append(now_html)
	}
	$("#search-result-box").slideDown()
}
