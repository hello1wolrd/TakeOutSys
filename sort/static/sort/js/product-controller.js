
angular.module('app')
    .factory('product_key', function($http, $q){
        return function(url, key, page){
            tmp_url = url + key + '/' + page;

            return $http.get(tmp_url)
                .then(function(response){
                    return response.data;
                }, function(response){
                    return $q.reject(response.status + " " +response.data.error);
                });
        }
    })
    .controller('ProductController', function($scope, $http, product_key){
        $scope.url = '/product/key/'
        $scope.key = ''
        $scope.page = ''
        $scope.products = []

        $scope.getProducts() = function(){
            product_key($scope.url, $scope.key, $scope.page)
                .then(function(products){
                    $scope.products = products;
                }, function(notice){
                    $scope.notice = notice;
                });
        }

    });
