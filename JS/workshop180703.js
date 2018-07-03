vis = {
  const svg = d3.select(DOM.svg(width, height));
 
  //create circles
  var my_circles = svg.selectAll("circle")
    .data([10,20,30]);
  my_circles.enter()
    .append("circle")
    .merge(my_circles)
      .attr("cx",function(d,i){
        return i*300 + 25;
      })
      .attr("cy",100)
      .attr("r",function(d){
        return d;
      })
      .attr("stroke","red")
      .attr("stroke",function(d,i){
        var st_color = "red";
        if (i == 0){
          st_color = "blue";
        }
        return st_color;
      })
      .attr("stroke-width", 10);
  my_circles.exit().remove();

  // create rectangles
  var my_rec = svg.selectAll("rect")
    .data([10,20,30]);
  my_rec.enter()
    .append("rect")
    .merge(my_rec)
      .attr("x", function(d,i){
        return i*(25+1);
      })
      .attr("y", function(d,i){
        return 100 - d;
      })
      .attr("width", 25)
      .attr("height", function(d){
        return d;
      })
  my_rec.exit().remove();
  
    return svg.node();
}
