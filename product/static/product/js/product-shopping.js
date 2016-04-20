var app = angular.module('app');

app.value('cart', []);

app.factory('handleCart', function(cart){
	var basecart = function(){};

	basecart.checkItem = function(id, price, title, count){
		del = false;
		add = false;
		remain_count = 0;

		cart.map(function(item, index){
			if (item.id === id){
				item.buy_count += count;
				if (item.buy_count <= 0){
					cart.splice(index, 1);
					remain_count = 0;
					console.log('delete a item');
					del = true;

				}else{
					item.price = item.buy_count * item.singleprice;
					cart[index].buy_count = item.buy_count;
					cart[index].price = item.price;
					remain_count = item.buy_count;
					console.log('count : ' + count);
					add = true;
				}
			}
		});

		if (add || del){
			return remain_count;
		}
		cart.push({id:id, singleprice:price, total:price, buy_count:1, title:title});
		console.log('add new item');
		return 1;		
	}

	basecart.addProduct = function(id, price, title){
		return basecart.checkItem(id, price, title, 1);
	}

	basecart.reduceProduct = function(id, price, title){
		return basecart.checkItem(id, price, title, -1)
	}

	return basecart;
});

app.directive('itemshow', function(){
	return {
		restrict: 'E',
		scope: {
			id: '@',
			title: '@',
			price: '@',
			imgurl: '@',
			description: '@',
			inventory: '=',
		},
		templateUrl: "/static/product/html/itemShow.html",
		controller: function($scope, cart, handleCart) {
			$scope.buy_qty = 0;
			$scope.inventory;


			$scope.addProduct = function(){
				if ($scope.inventory <= 0){
					return;
				}
				$scope.inventory -= 1;
				$scope.buy_qty = handleCart.addProduct($scope.id, $scope.price, $scope.title);
			};

			$scope.reduceProduct = function(){
				if($scope.buy_qty <= 0){
					return ;
				}
				$scope.inventory += 1;
				$scope.buy_qty = handleCart.reduceProduct($scope.id);

			};
		}
	}
});

app.directive('cartList', function(){
	return {
		restrict: 'E',
		templateUrl: '/static/product/html/cartList.html',
		controller: function($scope, cart){
			$scope.cart = cart;
		}
	}
});