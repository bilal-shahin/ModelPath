$(function () {
    let element = $('#container-01');
    let config = { backgroundColor: '#ddD' }; //
    let viewer = $3Dmol.createViewer(element, config);
    let met_id = document.getElementById('container-01').getAttribute('value');
    let pdbUri = "/static/images/pdb_files/" + met_id + ".pdb";
    jQuery.ajax(pdbUri, {
        success: function (data) {
            let v = viewer;
            v.addModel(data, "pdb");                       /* load data */
            v.setStyle({}, { stick: { color: 'spectrum' } });  /* style all atoms */
            v.zoomTo();                                      /* set camera */
            v.render();                                      /* render scene */
            v.zoom(1.2, 1000);                               /* slight zoom */
        },
        error: function (hdr, status, err) {
            console.error("Failed to load PDB " + pdbUri + ": " + err);
        },
    });
});