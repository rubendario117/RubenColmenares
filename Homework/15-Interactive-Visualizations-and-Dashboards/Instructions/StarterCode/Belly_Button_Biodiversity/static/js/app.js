function buildMetadata(sample) {
var url = '/metadata/' + sample;

  // @TODO: Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the metadata for a sample
    // Use d3 to select the panel with id of `#sample-metadata`
    d3.json(url).then(function (data) {
    var selector = d3.select("#sample-metadata");

    // Use `.html("") to clear any existing metadata
    sample_panel.html("");

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
    Object.entries(data).forEach(([key, value]) => {
      selector.append("h4").text(`${key}: ${value}`);
    });
  });
}

function buildCharts(sample) {

 // @TODO: Use `d3.json` to fetch the sample data for the plots
 var url = '/samples/' + sample;
 console.log("Url", url);
 // @TODO: Build a Bubble Chart using the sample data
 d3.json(url).then(function (data) {
   console.log("data", data);
   // @TODO: Build a Pie Chart

   var layout = {
     title: "Bacterial Samples"
   };
   // HINT: You will need to use slice() to grab the top 10 sample_values,
   // otu_ids, and labels (10 each).
   var pie_chart = [{
     values: data.sample_values.slice(0, 11),
     labels: data.otu_ids.slice(0, 11),
     type: "pie"
   }];

   Plotly.newPlot("pie", pie_chart, layout);

   var trace = [{
     x: data.otu_ids,
     y: data.sample_values,
     text: data.otu_labels,
     mode: 'markers',
     marker: {
       size: data.sample_values,
       color: data.otu_ids
     }
   }];
   var layout2 = {
     title: "Bubble Chart",
     showlegend: false
   };
   Plotly.newPlot("bubble", trace, layout2);

 })
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();