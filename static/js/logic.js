var ClassTypeChart = dc.rowChart("#ClassType");
var GeneTypeChart = dc.rowChart("#GeneType");
var VariationChart = dc.pieChart("#VariationCount")
d3.json("/gene_variants").then(function(data){


    // console.log(data);
    var new_data= crossfilter(data);
    var all = new_data.groupAll();

    var geneType = new_data.dimension(function(d){return d["Gene"];});
    var classType = new_data.dimension(function(d){return d ["Class"];});
    var variationType = new_data.dimension(function(d){return d ["Variation"]});

    var geneTypeGroup = geneType.group();
    var classTypeGroup = classType.group();
    var VariationTypeGroup = variationType.group();

    ClassTypeChart
        .height(300)
        .width(500)
        .dimension(classType)
        .group(classTypeGroup)
        .transitionDuration(500)
        .elasticX(true);

    GeneTypeChart
        .height(500)
        .width(500)
        .dimension(geneType)
        .group(geneTypeGroup)
        .transitionDuration(900)
        .elasticX(true)
        .data(function(group){ return group.top(20);});

    VariationChart
        .width(300)
        .height(400)
        .radius(140)
        .innerRadius(40)
        .dimension(variationType)
        .group(VariationTypeGroup)
        .transitionDuration(1200)
        .data(function(group){ return group.top(5);});
        
    
    dc.renderAll();

});

