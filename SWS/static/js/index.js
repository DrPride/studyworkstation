$(function () {
    //页面加载完成之后执行
    pageInit();
});

function pageInit() {
    //创建jqGrid组件
    jQuery("#list").jqGrid(
        {
            url: 'data/datagrid_data.json',//组件创建完成之后请求数据的url
            datatype: "json",//请求数据返回的类型。可选json,xml,txt
            colNames: ['学号', '姓名', '性别', '出生日期', '民族', '政治面貌', '学院', '专业', '班级'],//jqGrid的列显示名字
            colModel: [ //jqGrid每一列的配置信息。包括名字，索引，宽度,对齐方式.....
                {name: 'Id', index: 'Id', width: 100, align: "center"},
                {name: 'Name', index: 'Name', width: 100, align: "center"},
                {name: 'Gender', index: 'Gender', width: 80, align: "center"},
                {name: 'Birth', index: 'Birth', width: 120, align: "center"},
                {name: 'Nationality', index: 'Nationality', width: 100, align: "center"},
                {name: 'Political', index: 'Political', width: 150, align: "center"},
                {name: 'College', index: 'College', width: 150, align: "center"},
                {name: 'Profession', index: 'Profession', width: 150, align: "center"},
                {name: 'Class', index: 'Class', width: 150, align: "center"}
            ],
            rowNum: 10,//一页显示多少条
            rowList: [10, 20, 30],//可供用户选择一页显示多少条
            pager: '#pager',//表格页脚的占位符(一般是div)的id
            sortname: 'Id',//初始化的时候排序的字段
            gridview: true,
            loadonce: true,
            rownumbers: true,
            sortorder: "asc",//排序方式,可选desc,asc
            mtype: "get",//向后台请求数据的ajax的类型。可选post,get
            viewrecords: true,
            multiselect: true, //多行选择
            caption: "学生信息",//表格的标题名字
        });
    /*创建jqGrid的操作按钮容器*/
    /*可以控制界面上增删改查的按钮是否显示*/
    jQuery("#list").jqGrid('filterToolbar', {searchOperators: true});
    jQuery("#list").jqGrid('setGridHeight','100%');
    jQuery("#list").jqGrid('navGrid', '#pager', {edit: false, add: false, del: false});
}
