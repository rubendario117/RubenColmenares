var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;


var svg = d3.select(".chart")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);


// Get Data
d3.csv("assets/data/data.csv", function(err, datacsv) {
  if (err) throw err;

   datacsv.forEach(function(data) {
    data.income = +data.income;
    data.age = +data.age;
    data.healthcare = +data.healthcare;
    data.obesity = +data.obesity;
    data.smokes = +data.smokes;
    data.poverty = +data.poverty;
  });

  var xLinearScale = d3.scaleLinear()
    .domain([d3.min(datacsv, d => d.income - 5000), d3.max(datacsv, d => d.income + 5000)])
    .range([0, width]);

  var yLinearScale = d3.scaleLinear()
    .domain([d3.min(datacsv, d=> d.obesity - 5), d3.max(datacsv, d => d.obesity)])
    .range([height, 0]);

  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);

  chartGroup.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);

  chartGroup.append("g")
    .call(leftAxis);


  var circlesGroup = chartGroup.selectAll("circle")
  .data(datacsv)
  .enter()
  .append("circle")
  .attr("cx", d => xLinearScale(d.income))
  .attr("cy", d => yLinearScale(d.obesity))
  .attr("r", "15")
  .attr("fill", "lightblue")
  .attr("opacity", "1");


    chartGroup.append("text")
    .selectAll("tspan")
    .data(datacsv)
    .enter()
    .append("tspan")
        .attr("x", d => xLinearScale(d.income))
        .attr("y", d => yLinearScale(d.obesity))
        .attr("text-anchor", "middle")
        .text(function(data) {
            return data.abbr
        })
        .attr("fill", "white")
        .attr("font-size", 10, "bold");


  var toolTip = d3.tip()
    .attr("class", "tooltip")
    .offset([80, -60])
    .html(function(d) {
      return (`${d.state}<br>Income (Median): $${d.income}<br>Obesity: ${d.obesity}%`);
    });


  chartGroup.call(toolTip);


  circlesGroup.on("click", function(data) {
    toolTip.show(data);
  })

    .on("mouseout", function(data, index) {
      toolTip.hide(data);
    });

  chartGroup.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left + 40)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .attr("class", "axisText")
    .text("Obesity (%)");

  chartGroup.append("text")
    .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
    .attr("class", "axisText")
    .text("Houshold Income (Median)");

    // LABELS //
  var toolTip = d3.select("body").append("div")
    .attr("class", "tooltip");

  circlesGroup.on("mouseover", function(d, i) {
    toolTip.style("display", "block");
    toolTip.html(`<strong>${d.state}</strong><br>Income: $${d.income}<br> Obesity: ${d.obesity}%`)
      .style("left", d3.event.pageX + "px")
      .style("top", d3.event.pageY + "px");
  })

    .on("mouseout", function() {
      toolTip.style("display", "none");
    });
});