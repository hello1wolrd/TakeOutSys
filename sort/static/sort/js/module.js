var app = angular.module('app', ['ngFileUpload']);

 app.factory('csrfTokenInterceptor', function () {
    var csrfToken = null;
     return {
       response: function (response) {
          csrftoken = Cookies.get('csrftoken');
          return response;
       },
       request: function (config) {
         if (config.method == 'POST' && csrftoken) {
           config.headers["X-CSRFToken"] = csrftoken;
         }
         return config;
       }
     }
  });

 app.config(function ($httpProvider) {
    $httpProvider.interceptors.push('csrfTokenInterceptor');
  });