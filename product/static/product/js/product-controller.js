
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
                        alert("nonono");
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
   .controller('ImageChangeController', function($scope, $http){
        $scope.img_count = angular.element('#image-change .img-change').length;
        
        var reader = new FileReader();
        imgs = angular.element('#image-change .img-change');
        imgs.change(function(e){
            var reader = new FileReader();
            parent = $(this).parent().get(0);
            img_doc = $('#'+parent.id).children('img').get(0);
            reader.onload = function(e) {
                img_doc.src = e.target.result;
            };
            reader.readAsDataURL($(this)[0].files[0]);
        });
   });
 
