angular.module('opal.controllers').controller(
    'AllocatedClinicLocationHelper',
    function(
      $scope, $window, recordLoader, ngProgressLite, $q,
      $route, Metadata
    ){
      "use strict";
      var self = this;
      var allocated_clinic;
      self.saving = false;
      self.editing = {allocated_clinic: {}};

      Metadata.then(function(metadata){
        self.metadata = metadata;
      });

      recordLoader.then(function(){
        if($scope.episode.allocated_clinic && $scope.episode.allocated_clinic.length){
          allocated_clinic = $scope.episode.allocated_clinic[0];
        }
        else{
          allocated_clinic = $scope.episode.newItem("allocated_clinic");
        }
        var changed = allocated_clinic.makeCopy();
        self.editing.allocated_clinic = changed;

        self.submit = function(){
            self.saving = true;
            allocated_clinic.save(changed).then(function(){
                self.saving = false;
                $route.reload();
            });
          };
        });
      });
