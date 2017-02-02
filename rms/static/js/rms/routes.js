var app = angular.module('opal');
app.controller('WelcomeCtrl', function(){});

app.config(
    ['$routeProvider',
     function($routeProvider){
//	     $routeProvider.when('/',  {redirectTo: '/list'})

         $routeProvider.when('/',  {
             controller: 'WelcomeCtrl',
             templateUrl: '/templates/welcome.html'}
                            )
             .when('/overview', {
                 controller: 'WelcomeCtrl',
                 templateUrl: '/templates/overview.html'
             })
             .when('/myclinic', {
                 controller: 'WelcomeCtrl',
                 templateUrl: '/templates/my_clinic.html'
             })
     }]);
