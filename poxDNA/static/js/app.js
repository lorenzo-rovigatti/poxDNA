'use strict';

// Declare app level module which depends on views, and components
angular.module('poxDNA', [
  'ngRoute',
  'poxDNA.home',
  'poxDNA.login'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider
  .otherwise({redirectTo: '/'});
}]);
