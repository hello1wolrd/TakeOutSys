
angular.module('app')
    .factory('product_key', function($http, $q){
        return function(url, key, page){
            tmp_url = url + key + '/' + page;

            return $http.get(tmp_url)
                .then(function(response){
                    console.log(response.data);
                    return response.data;
                }, function(response){
                    return $q.reject(response.status + " " +response.data.error);
                });
        }
    })
    .directive('productlist', function(){
        return{
            restrict: 'E',
            templateUrl: "/static/product/html/productlist.html",
            link: function(scope, element, attrs){

            }
            
        }
    })
    .controller('ProductController', function($scope, $http, $document, product_key){
        $scope.url = '/product/key/';
        $scope.key = '';
        $scope.page = 0;
        $scope.notice = '';
        $scope.products = [];
        $scope.show = false;

        $scope.getpage = function(page){ 

            product_key($scope.url, $scope.key, page)
                .then(function(data){
                    tmp_products = data.products;
                    console.log(tmp_products);
                    if (tmp_products.length == 0){
                        alert("nothing here");
                        return ;
                    }
                    $scope.products = tmp_products;
                    $scope.page = page;
                }, function(notice){
                    $scope.notice = notice;
                });
        };

        $scope.submit = function(){
            doc = angular.element('#main-body');
            doc.remove();
            $scope.show = true;
 
            $scope.page = 1;
            $scope.getpage($scope.page);
        };

        $scope.pre = function() {
            page = parseInt($scope.page);
            pre_page = page - 1;
            if (pre_page <= 0){
                return;
            }
            
            $scope.getpage($scope.page - 1);
        };

        $scope.next = function(){
            $scope.getpage($scope.page + 1);
        };


    })
    .factory('handleName', function(){

        var basehandler = function(){};

        basehandler.changename = function(name, operate){
            res = name.split('-');
            res[0] = operate;
            new_name = res.join('-');
            return new_name;
        };

        basehandler.modifyname = function(scope){
            scope.id = basehandler.changename(scope.id, 'modify');
        };

        basehandler.deletename = function(scope){
            console.log('>>>>>> deletename');
            scope.id = basehandler.changename(scope.id, 'delete');
        };

        basehandler.addname = function(scope){
            scope.id = basehandler.changename(scope.id, 'add');
        };

        return basehandler;
    })
    .value("imagelist", [])
    .value("globalid", 0)
    .directive("newImageList", function(){
        return {
            resctrict: 'E',
            templateUrl: '/static/product/html/newimagelist.html',
        }
    })
    .controller('NewImageListController', function($scope, $element, handleName, imagelist, globalid){
        
        $scope.fieldshow = true;
        $scope.imagelist = imagelist;

        $scope.addnew = function(){
            var id = '7dajfio' + (globalid++).toString();
            imginfo = {'id': id};
            imagelist.push(imginfo);
        }

    })
    .directive("imageSingle", function(){
       return {
           resctrict: 'E',
           templateUrl: '/static/product/html/imageinfo.html',
           transclude: true,
           scope: {
                imgurl: '@',
                imgdes: '@',
                id: '=',
                fieldshow: '=',
                delete: '&',
                modify: '&',
           },
       } 
    })
    .controller('SingleImageController', function($scope, $element, handleName, imagelist){
        
        $scope.fieldshow = true;

        $scope.initold = function(id){

            $scope.id = 'old-' + id;
        }

        $scope.initnew = function(id){
            
            $scope.raw_id = id;
            $scope.id = 'new-' + id;
            console.log("add new id: " + $scope.id);
        }

        $scope.delete = function(){
            console.log('>>>>>> delete name');
            $scope.fieldshow = false;
            handleName.deletename($scope);
        };

        $scope.delete_element = function(){
            console.log('>>>>>> delete element');
            imagelist.map(function(item, index){
                console.log(item);

                if (item.id === $scope.raw_id){
                    imagelist.splice(index, 1);
                    console.log('>>>>>> delete list');
                }
            });
            
        };

        $scope.modify = function(){
            console.log(">>>>>> modify");
            handleName.modifyname($scope);
        }
    })
    .directive("imageMultiple", function(){
        return {
            transclude: true,
            resctrict: 'E',
            templateUrl: '/static/product/html/imagelist.html',
            scope: {
                addnew: '&',
            }
        }
    })
    .directive('insideTest', function(){
        return {
            resctrict:'E',
            template: '<span>value: {{val}}, title: {{title}}</span>',
            transclude: true,
            scope: {
                title: '@',
                val: '=',
            },
    } 
    })
    .controller('insideController', function($scope){
        $scope.val;
        
        $scope.init = function(val){alert(val);$scope.val=val;};
    });
