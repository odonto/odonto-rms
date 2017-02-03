angular.module('opal.controllers').controller(
  'AllocatedClinicLocationHelper',
  function(
    $scope, $window, recordLoader, ngProgressLite, $q,
    $route){
    "use strict";
    var self = this;
    var allocated_clinic;
    self.saving = false;
    self.editing = {allocated_clinic: {}};
    self.confirmed = false;

    recordLoader.then(function(){
      if($scope.episode.allocated_clinic && $scope.episode.allocated_clinic.length){
        allocated_clinic = $scope.episode.allocated_clinic[0];
      }
      else{
        allocated_clinic = $scope.episode.newItem("allocated_clinic");
      }
      var changed = allocated_clinic.makeCopy();
      self.submitted = allocated_clinic.location_id;
      self.confirmed = allocated_clinic.confirmed;
      self.editing.allocated_clinic = changed;

      $scope.$watch('allocatedClinicLocationHelper.editing.allocated_clinic.location_id', function() {
        self.confirmed = false;
        self.submitted = false;
      });

      self.confirm = function(){
        changed.confirmed = true;
        self.saving = true;
        self.confirmed = true;
        allocated_clinic.save(changed).then(function(){
          self.saving = false;
          self.editing.allocated_clinic =  $scope.episode.allocated_clinic[0].makeCopy();
        });
      }
      self.submit = function(){
        self.saving = true;
        self.submitted = true;
        allocated_clinic.save(changed).then(function(){
          self.saving = false;
          self.editing.allocated_clinic =  $scope.episode.allocated_clinic[0].makeCopy();
        });
      };
    });
  });
