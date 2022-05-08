aa
function draw_legend(){
  var lsvg = d3.select("body").append("svg")
    .attr("id", "lsvg")
    .attr("width", width)
    .attr("height", height)

  // create a list of keys
  var keys = ['ماشين آلات و دستگاه\u200cهاي برقي',
 'لاستيك و پلاستيك',
 'سرمايه گذاريها',
 'ماشين آلات و تجهيزات',
 'انبوه سازي، املاك و مستغلات',
 'انتشار، چاپ و تکثير',
 'محصولات چوبي',
 'محصولات كاغذي',
 'حمل ونقل، انبارداري و ارتباطات',
 'خودرو و ساخت قطعات',
 'مواد و محصولات دارويي',
 'رايانه و فعاليت\u200cهاي وابسته به آن',
 'خدمات فني و مهندسي',
 'سيمان، آهك و گچ',
 'محصولات شيميايي',
 'فراورده هاي نفتي، كك و سوخت هسته اي',
 'محصولات غذايي و آشاميدني به جز قند و شكر',
 'ساخت محصولات فلزي',
 'فلزات اساسي',
 'قند و شكر',
 'ساير محصولات كاني غيرفلزي',
 'استخراج کانه هاي فلزي',
 'كاشي و سراميك',
 'استخراج زغال سنگ',
 'ساخت دستگاه\u200cها و وسايل ارتباطي',
 'منسوجات',
 'شرکتهاي چند رشته اي صنعتي',
 'بانكها و موسسات اعتباري',
 'ساير واسطه گريهاي مالي']

var my_colors = colors = ["#ab0cff", "#3283ff", "#85660c", "#782ab7",
                "#565656", "#1c8356", "#16ff32", "#f8e2a1",
                "#e3e3e3", "#1cbf4e", "#c5441c", "#dfa1fe",
                "#fc00f8", "#325a9b", "#ffb116", "#f9a19f",
                "#91ad1c", "#91ad1c", "#91ad1c", "#2ed9ff",
                "#b10ca1", "#c174a7", "#fe1cbf", "#b10068",
                "#fae326", "#fb0087", "#87556f", "#322f3d",
                "#eebb4d"]

  // Add one dot in the legend for each name.
  svg.selectAll("mydots")
    .data(keys)
    .enter()
    .append("circle")
      .attr("cx", 10)
      .attr("cy", function(d,i){ return 100 + i*25}) // 100 is where the first dot appears. 25 is the distance between dots
      .attr("r", 7)
      .style("fill", function(d, i){ return my_colors[i]})

  // Add one dot in the legend for each name.
  svg.selectAll("mylabels")
    .data(keys)
    .enter()
    .append("text")
      .attr("x", 30)
      .attr("y", function(d,i){ return 105 + i*25}) // 100 is where the first dot appears. 25 is the distance between dots
      .style("fill", function(d, i){ return my_colors[i]})
      .text(function(d){ return d})
      .attr("text-anchor", "left")
      .style("alignment-baseline", "middle")

}

//code before the pause
setTimeout(function(){
    draw_legend()
}, 10000);