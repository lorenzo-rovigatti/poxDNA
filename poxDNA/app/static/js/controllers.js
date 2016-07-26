'use strict';

// Home page
angular.module('poxDNA.home', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/', {
    templateUrl: 'static/partials/landing.html',
    controller: 'HomeCtrl'
  });
}])
.controller('HomeCtrl', [function() {

}]);

// Login
angular.module('poxDNA.login', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/login', {
    templateUrl: 'static/partials/login.html',
    controller: 'LoginCtrl'
  });
}])

.controller('LoginCtrl', [function() {

}]);
