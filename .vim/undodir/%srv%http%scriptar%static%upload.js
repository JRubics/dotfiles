Vim�UnDo� v�����
G7�$��r��'�3aD_�J�S�   =   		if ($("#script_link").val()){                             X��1    _�                            ����                                                                                                                                                                                                                                                                                                                                                             X���     �         :    �         :    5�_�                       $    ����                                                                                                                                                                                                                                                                                                                                                             X���     �         ;      @        formData.append('description', $("#description").val());5�_�                       6    ����                                                                                                                                                                                                                                                                                                                                                             X���     �         ;      @        formData.append('script_link', $("#description").val());5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X���     �         ;      @        formData.append('script_link', $("#script_link").val());5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             X���     �         <              5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                             X���     �         <              if()5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             X���     �         <              if ()5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                               !          8       v   >    X���     �         <              if ()�         <    5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                               !          8       v   >    X��     �         <      %        if ()$("#script_link").val())5�_�   
                    $    ����                                                                                                                                                                                                                                                                                                                               !          8       v   >    X��     �         <      $        if ($("#script_link").val())5�_�                           ����                                                                                                                                                                                                                                                                                                                               !          8       v   >    X��     �                :		formData.append('script_link', $("#script_link").val());5�_�                            ����                                                                                                                                                                                                                                                                                                                               !          8       v   >    X��     �         =    �         =    5�_�                            ����                                                                                                                                                                                                                                                                                                                             !          8       v   >    X��     �   <   >              }�   :   <                  });�   9   ;                      }�   8   :                          return xhr;�   6   8                          }, false);�   4   6                              }�   2   4                                  }�   1   3          <                            $('.progress-bar').html('Done');�   0   2          6                        if (percentComplete === 100) {�   /   1          Z                        // once the upload reaches 100%, set the progress bar text to done�   -   /          H                        $('.progress-bar').width(percentComplete + '%');�   ,   .          G                        $('.progress-bar').text(percentComplete + '%');�   +   -          T                        // update the Bootstrap progress bar with the new percentage�   )   +          J                        percentComplete = parseInt(percentComplete * 100);�   (   *          E                        var percentComplete = evt.loaded / evt.total;�   '   )          G                        // calculate the percentage of upload completed�   &   (          /                    if (evt.lengthComputable) {�   $   &          G                xhr.upload.addEventListener('progress', function(evt) {�   #   %          1                // listen to the 'progress' event�   !   #          /                var xhr = new XMLHttpRequest();�       "          +                // create an XMLHttpRequest�      !                      xhr: function() {�                             },�                ;                console.log('upload successful!\n' + data);�                $            success: function(data){�                            contentType: false,�                            processData: false,�                            data: formData,�                            type: 'POST',�                            url: '/upload',�                        $.ajax({�                :		formData.append('script_link', $("#script_link").val());�                %        if ($("#script_link").val()){�                @        formData.append('description', $("#description").val());�                @        formData.append('script_name', $("#script_name").val());�                	        }�                9            formData.append('file' + i, file, file.name);�   
                          var file = files[i];�   	             0        for (var i = 0; i < files.length; i++) {�      	          &        var formData = new FormData();�                    if (files.length > 0){�                0    var files = $("#upload-input").get(0).files;�                #    $('.progress-bar').width('0%');�                "    $('.progress-bar').text('0%');�                    event.preventDefault();5�_�                            ����                                                                                                                                                                                                                                                                                                                             !          8       v   >    X��     �         >       5�_�                            ����                                                                                                                                                                                                                                                                                                                             !          8       v   >    X��     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                             !          8       v   >    X��0    �         =      		if ($("#script_link").val()){5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             X���     �         :    �         :      @        formData.append('description', $("#description").val());5��