ClassicEditor
            .create( document.querySelector( '#id_blog_content' ) )
            .catch( error => {
                console.error( error );
            } );