(function () {
  "use strict";

  var renderer, scene, camera, group, shell, points, rings = [], ready = false;

  function init(opts) {
    if (ready || !window.THREE || !opts || !opts.container) return;

    var THREE = window.THREE;
    renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, preserveDrawingBuffer: true });
    renderer.setPixelRatio(1);
    renderer.setSize(820, 820, false);
    renderer.setClearColor(0xffffff, 0);
    renderer.domElement.setAttribute("aria-hidden", "true");
    opts.container.appendChild(renderer.domElement);

    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(28, 1, 0.1, 100);
    camera.position.set(0, 0, 8.6);

    group = new THREE.Group();
    scene.add(group);

    var geometry = new THREE.IcosahedronGeometry(2.05, 2);
    shell = new THREE.Mesh(
      geometry,
      new THREE.MeshBasicMaterial({ color: 0x060606, wireframe: true, transparent: true, opacity: 0.46 })
    );
    group.add(shell);

    points = new THREE.Points(
      geometry,
      new THREE.PointsMaterial({ color: 0x060606, size: 0.075, sizeAttenuation: true, transparent: true, opacity: 0.95 })
    );
    group.add(points);

    [[2.75, 0.0], [3.18, Math.PI / 3], [3.62, -Math.PI / 3]].forEach(function (entry, i) {
      var ring = new THREE.Mesh(
        new THREE.TorusGeometry(entry[0], 0.012 + i * 0.004, 6, 160),
        new THREE.MeshBasicMaterial({ color: i === 1 ? 0x5d5d5d : 0x060606, transparent: true, opacity: 0.58 })
      );
      ring.rotation.x = entry[1];
      ring.rotation.y = Math.PI / 5 + i * 0.42;
      rings.push(ring);
      group.add(ring);
    });

    var lightDotGeometry = new THREE.SphereGeometry(0.08, 10, 10);
    for (var d = 0; d < 18; d++) {
      var a = d * 2.399963;
      var z = 1 - (2 * d) / 17;
      var r = Math.sqrt(Math.max(0, 1 - z * z));
      var dot = new THREE.Mesh(lightDotGeometry, new THREE.MeshBasicMaterial({ color: 0x060606 }));
      dot.position.set(Math.cos(a) * r * 3.2, Math.sin(a) * r * 2.1, z * 1.1);
      dot.userData.phase = d * 0.31;
      group.add(dot);
    }

    ready = true;
    setTime(0);
  }

  function setTime(t) {
    if (!ready) return;
    group.rotation.y = t * 0.21;
    group.rotation.x = -0.18 + Math.sin(t * 0.34) * 0.09;
    shell.rotation.z = t * 0.055;
    points.rotation.z = -t * 0.035;
    rings.forEach(function (ring, i) {
      ring.rotation.z = (i % 2 ? -1 : 1) * t * (0.11 + i * 0.025);
    });
    group.children.forEach(function (child) {
      if (typeof child.userData.phase === "number") {
        var s = 0.72 + 0.28 * Math.sin(t * 2.2 + child.userData.phase);
        child.scale.setScalar(s);
      }
    });
    renderer.render(scene, camera);
  }

  window.__coreScene = { init: init, setTime: setTime };
})();
