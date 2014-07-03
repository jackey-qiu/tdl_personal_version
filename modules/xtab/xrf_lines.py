"""
X-ray fluorescence lines
"""
########################################################################

xrf_lines = {"H":{"KA":0.000,"KA1":0.000,"KA2":0.000,"KB":0.000,"KB1":0.000,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "HE":{"KA":0.000,"KA1":0.000,"KA2":0.000,"KB":0.000,"KB1":0.000,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "LI":{"KA":0.052,"KA1":0.000,"KA2":0.000,"KB":0.000,"KB1":0.000,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "BE":{"KA":0.110,"KA1":0.000,"KA2":0.000,"KB":0.000,"KB1":0.000,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "B":{"KA":0.185,"KA1":0.000,"KA2":0.000,"KB":0.000,"KB1":0.000,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "C":{"KA":0.282,"KA1":0.000,"KA2":0.000,"KB":0.000,"KB1":0.000,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "N":{"KA":0.392,"KA1":0.000,"KA2":0.000,"KB":0.000,"KB1":0.000,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "O":{"KA":0.523,"KA1":0.000,"KA2":0.000,"KB":0.000,"KB1":0.000,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "F":{"KA":0.677,"KA1":0.000,"KA2":0.000,"KB":0.000,"KB1":0.000,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "NE":{"KA":0.851,"KA1":0.000,"KA2":0.000,"KB":0.000,"KB1":0.000,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "NA":{"KA":1.041,"KA1":1.041,"KA2":1.041,"KB":1.071,"KB1":1.067,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "MG":{"KA":1.254,"KA1":1.253,"KA2":1.254,"KB":1.302,"KB1":1.297,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "AL":{"KA":1.487,"KA1":1.486,"KA2":1.486,"KB":1.557,"KB1":1.553,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "SI":{"KA":1.740,"KA1":1.740,"KA2":1.739,"KB":1.838,"KB1":1.832,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "P":{"KA":2.015,"KA1":2.013,"KA2":2.014,"KB":2.142,"KB1":2.136,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "S":{"KA":2.307,"KA1":2.307,"KA2":2.306,"KB":2.468,"KB1":2.464,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "CL":{"KA":2.622,"KA1":2.622,"KA2":2.621,"KB":2.817,"KB1":2.815,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "AR":{"KA":2.957,"KA1":2.957,"KA2":2.955,"KB":3.191,"KB1":3.192,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "K":{"KA":3.312,"KA1":3.313,"KA2":3.310,"KB":3.589,"KB1":3.589,"KB2":0.000,"LA1":0.000,"LB1":0.000,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "CA":{"KA":3.690,"KA1":3.691,"KA2":3.688,"KB":4.012,"KB1":4.012,"KB2":0.000,"LA1":0.341,"LB1":0.344,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "SC":{"KA":4.088,"KA1":4.090,"KA2":4.085,"KB":4.459,"KB1":4.460,"KB2":0.000,"LA1":0.395,"LB1":0.399,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "TI":{"KA":4.508,"KA1":4.510,"KA2":4.504,"KB":4.931,"KB1":4.931,"KB2":0.000,"LA1":0.452,"LB1":0.458,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "V":{"KA":4.949,"KA1":4.951,"KA2":4.944,"KB":5.427,"KB1":5.427,"KB2":0.000,"LA1":0.510,"LB1":0.519,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "CR":{"KA":5.411,"KA1":5.414,"KA2":5.405,"KB":5.947,"KB1":5.946,"KB2":0.000,"LA1":0.571,"LB1":0.581,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "MN":{"KA":5.895,"KA1":5.898,"KA2":5.887,"KB":6.492,"KB1":6.490,"KB2":0.000,"LA1":0.636,"LB1":0.647,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "FE":{"KA":6.400,"KA1":6.403,"KA2":6.390,"KB":7.059,"KB1":7.057,"KB2":0.000,"LA1":0.704,"LB1":0.717,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "CO":{"KA":6.925,"KA1":6.929,"KA2":6.915,"KB":7.649,"KB1":7.649,"KB2":0.000,"LA1":0.775,"LB1":0.790,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "NI":{"KA":7.472,"KA1":7.477,"KA2":7.460,"KB":8.265,"KB1":8.264,"KB2":8.328,"LA1":0.849,"LB1":0.866,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "CU":{"KA":8.041,"KA1":8.046,"KA2":8.027,"KB":8.907,"KB1":8.904,"KB2":8.976,"LA1":0.928,"LB1":0.948,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "ZN":{"KA":8.631,"KA1":8.637,"KA2":8.615,"KB":9.572,"KB1":9.571,"KB2":9.657,"LA1":1.009,"LB1":1.032,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "GA":{"KA":9.243,"KA1":9.250,"KA2":9.234,"KB":10.263,"KB1":10.263,"KB2":10.365,"LA1":1.098,"LB1":1.125,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "GE":{"KA":9.876,"KA1":9.885,"KA2":9.854,"KB":10.984,"KB1":10.981,"KB2":11.100,"LA1":1.188,"LB1":1.218,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "AS":{"KA":10.532,"KA1":10.542,"KA2":10.507,"KB":11.729,"KB1":11.725,"KB2":11.863,"LA1":1.282,"LB1":1.317,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "SE":{"KA":11.210,"KA1":11.220,"KA2":11.181,"KB":12.501,"KB1":12.495,"KB2":12.651,"LA1":1.379,"LB1":1.419,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "BR":{"KA":11.907,"KA1":11.922,"KA2":11.877,"KB":13.296,"KB1":13.290,"KB2":13.465,"LA1":1.480,"LB1":1.526,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "KR":{"KA":12.630,"KA1":12.648,"KA2":12.597,"KB":14.120,"KB1":14.112,"KB2":14.313,"LA1":1.586,"LB1":1.636,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "RB":{"KA":13.375,"KA1":13.393,"KA2":13.335,"KB":14.971,"KB1":14.960,"KB2":15.184,"LA1":1.694,"LB1":1.752,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "SR":{"KA":14.142,"KA1":14.163,"KA2":14.097,"KB":15.849,"KB1":15.834,"KB2":16.083,"LA1":1.806,"LB1":1.871,"LB2":0.001,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "Y":{"KA":14.933,"KA1":14.956,"KA2":14.882,"KB":16.754,"KB1":16.736,"KB2":17.011,"LA1":1.922,"LB1":1.995,"LB2":0.000,"LG1":0.000,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "ZR":{"KA":15.746,"KA1":15.772,"KA2":15.690,"KB":17.687,"KB1":17.665,"KB2":17.959,"LA1":2.042,"LB1":2.124,"LB2":2.219,"LG1":2.302,"LG2":2.503,"LG3":2.503,"LG4":0.000,"LL":1.792},
             "NB":{"KA":16.584,"KA1":16.612,"KA2":16.520,"KB":18.647,"KB1":18.621,"KB2":18.951,"LA1":2.166,"LB1":2.257,"LB2":2.367,"LG1":2.462,"LG2":2.664,"LG3":2.664,"LG4":0.000,"LL":1.902},
             "MO":{"KA":17.443,"KA1":17.476,"KA2":17.373,"KB":19.633,"KB1":19.607,"KB2":19.964,"LA1":2.293,"LB1":2.394,"LB2":2.518,"LG1":2.623,"LG2":2.831,"LG3":2.831,"LG4":0.000,"LL":2.016},
             "TC":{"KA":18.327,"KA1":18.364,"KA2":18.328,"KB":20.647,"KB1":20.585,"KB2":21.012,"LA1":2.424,"LB1":2.536,"LB2":2.674,"LG1":2.792,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "RU":{"KA":19.235,"KA1":19.276,"KA2":19.149,"KB":21.687,"KB1":21.655,"KB2":22.072,"LA1":2.558,"LB1":2.683,"LB2":2.835,"LG1":2.964,"LG2":3.181,"LG3":3.181,"LG4":0.000,"LL":2.253},
             "RH":{"KA":20.167,"KA1":20.213,"KA2":20.072,"KB":22.759,"KB1":22.721,"KB2":23.169,"LA1":2.696,"LB1":2.834,"LB2":3.001,"LG1":3.144,"LG2":3.364,"LG3":3.364,"LG4":0.000,"LL":2.377},
             "PD":{"KA":21.123,"KA1":21.174,"KA2":21.018,"KB":23.859,"KB1":23.816,"KB2":24.297,"LA1":2.838,"LB1":2.990,"LB2":3.171,"LG1":3.328,"LG2":3.553,"LG3":3.553,"LG4":0.000,"LL":2.503},
             "AG":{"KA":22.104,"KA1":22.159,"KA2":21.988,"KB":24.987,"KB1":24.942,"KB2":25.454,"LA1":2.984,"LB1":3.150,"LB2":3.347,"LG1":3.519,"LG2":3.743,"LG3":3.750,"LG4":0.000,"LL":2.634},
             "CD":{"KA":23.109,"KA1":23.170,"KA2":22.982,"KB":26.143,"KB1":26.093,"KB2":26.641,"LA1":3.133,"LB1":3.316,"LB2":3.528,"LG1":3.716,"LG2":3.951,"LG3":0.000,"LG4":0.000,"LL":2.767},
             "IN":{"KA":24.139,"KA1":24.206,"KA2":24.000,"KB":27.382,"KB1":27.274,"KB2":27.859,"LA1":3.286,"LB1":3.487,"LB2":3.713,"LG1":3.920,"LG2":4.161,"LG3":4.161,"LG4":4.237,"LL":2.904},
             "SN":{"KA":25.193,"KA1":25.267,"KA2":25.042,"KB":28.601,"KB1":28.483,"KB2":29.106,"LA1":3.443,"LB1":3.662,"LB2":3.904,"LG1":4.131,"LG2":4.377,"LG3":4.377,"LG4":4.464,"LL":3.045},
             "SB":{"KA":26.274,"KA1":26.355,"KA2":26.109,"KB":29.851,"KB1":29.723,"KB2":30.387,"LA1":3.604,"LB1":3.843,"LB2":4.100,"LG1":4.347,"LG2":4.560,"LG3":4.600,"LG4":4.697,"LL":3.188},
             "TE":{"KA":27.380,"KA1":27.468,"KA2":27.200,"KB":31.128,"KB1":30.993,"KB2":31.698,"LA1":3.769,"LB1":4.029,"LB2":4.301,"LG1":4.570,"LG2":4.829,"LG3":4.829,"LG4":4.937,"LL":3.336},
             "I":{"KA":28.512,"KA1":28.607,"KA2":28.315,"KB":32.437,"KB1":32.292,"KB2":33.016,"LA1":3.937,"LB1":4.220,"LB2":4.507,"LG1":4.800,"LG2":5.066,"LG3":5.066,"LG4":5.185,"LL":3.485},
             "XE":{"KA":29.669,"KA1":29.774,"KA2":29.485,"KB":33.777,"KB1":33.644,"KB2":34.446,"LA1":4.109,"LB1":4.422,"LB2":4.720,"LG1":5.036,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "CS":{"KA":30.854,"KA1":30.968,"KA2":30.623,"KB":35.149,"KB1":34.984,"KB2":35.819,"LA1":4.286,"LB1":4.619,"LB2":4.935,"LG1":5.280,"LG2":5.542,"LG3":5.553,"LG4":5.703,"LL":3.795},
             "BA":{"KA":32.065,"KA1":32.188,"KA2":31.815,"KB":36.553,"KB1":36.376,"KB2":37.255,"LA1":4.465,"LB1":4.827,"LB2":5.156,"LG1":5.531,"LG2":5.797,"LG3":5.809,"LG4":5.973,"LL":3.954},
             "LA":{"KA":33.302,"KA1":33.436,"KA2":33.033,"KB":37.986,"KB1":37.799,"KB2":38.728,"LA1":4.650,"LB1":5.041,"LB2":5.383,"LG1":5.789,"LG2":6.060,"LG3":6.074,"LG4":6.252,"LL":4.124},
             "CE":{"KA":34.569,"KA1":34.714,"KA2":34.276,"KB":39.453,"KB1":39.255,"KB2":40.231,"LA1":4.839,"LB1":5.261,"LB2":5.612,"LG1":6.052,"LG2":6.325,"LG3":6.341,"LG4":6.528,"LL":4.288},
             "PR":{"KA":35.864,"KA1":36.020,"KA2":35.548,"KB":40.953,"KB1":40.746,"KB2":41.772,"LA1":5.033,"LB1":5.488,"LB2":5.849,"LG1":6.322,"LG2":6.598,"LG3":6.616,"LG4":6.815,"LL":4.453},
             "ND":{"KA":37.185,"KA1":37.355,"KA2":36.845,"KB":42.484,"KB1":42.269,"KB2":43.298,"LA1":5.229,"LB1":5.721,"LB2":6.088,"LG1":6.602,"LG2":6.883,"LG3":6.902,"LG4":7.107,"LL":4.633},
             "PM":{"KA":38.535,"KA1":38.718,"KA2":38.160,"KB":44.049,"KB1":43.945,"KB2":44.955,"LA1":5.432,"LB1":5.960,"LB2":6.338,"LG1":6.891,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "SM":{"KA":39.914,"KA1":40.111,"KA2":39.523,"KB":45.649,"KB1":45.400,"KB2":46.553,"LA1":5.635,"LB1":6.205,"LB2":6.585,"LG1":7.180,"LG2":7.467,"LG3":7.487,"LG4":7.714,"LL":4.995},
             "EU":{"KA":41.323,"KA1":41.535,"KA2":40.877,"KB":47.283,"KB1":47.027,"KB2":48.241,"LA1":5.845,"LB1":6.455,"LB2":6.842,"LG1":7.478,"LG2":7.768,"LG3":7.796,"LG4":8.030,"LL":5.177},
             "GD":{"KA":42.761,"KA1":42.989,"KA2":42.280,"KB":48.949,"KB1":48.718,"KB2":49.961,"LA1":6.056,"LB1":6.712,"LB2":7.102,"LG1":7.788,"LG2":8.087,"LG3":8.105,"LG4":8.355,"LL":5.362},
             "TB":{"KA":44.229,"KA1":44.474,"KA2":43.737,"KB":50.650,"KB1":50.391,"KB2":51.737,"LA1":6.272,"LB1":6.977,"LB2":7.365,"LG1":8.104,"LG2":8.398,"LG3":8.423,"LG4":8.685,"LL":5.546},
             "DY":{"KA":45.728,"KA1":45.991,"KA2":45.193,"KB":52.384,"KB1":52.178,"KB2":53.491,"LA1":6.494,"LB1":7.246,"LB2":7.634,"LG1":8.418,"LG2":8.714,"LG3":8.753,"LG4":9.020,"LL":5.743},
             "HO":{"KA":47.257,"KA1":47.539,"KA2":46.686,"KB":54.155,"KB1":53.934,"KB2":55.292,"LA1":6.719,"LB1":7.524,"LB2":7.910,"LG1":8.748,"LG2":9.051,"LG3":9.087,"LG4":9.374,"LL":5.943},
             "ER":{"KA":48.818,"KA1":49.119,"KA2":48.205,"KB":55.963,"KB1":55.690,"KB2":57.088,"LA1":6.947,"LB1":7.809,"LB2":8.188,"LG1":9.089,"LG2":9.385,"LG3":9.431,"LG4":9.722,"LL":6.152},
             "TM":{"KA":50.410,"KA1":50.733,"KA2":49.762,"KB":57.806,"KB1":57.576,"KB2":58.969,"LA1":7.179,"LB1":8.100,"LB2":8.467,"LG1":9.424,"LG2":9.730,"LG3":9.779,"LG4":10.084,"LL":6.342},
             "YB":{"KA":52.035,"KA1":52.380,"KA2":51.326,"KB":59.687,"KB1":59.352,"KB2":60.959,"LA1":7.414,"LB1":8.400,"LB2":8.757,"LG1":9.779,"LG2":10.090,"LG3":10.143,"LG4":10.460,"LL":6.546},
             "LU":{"KA":53.693,"KA1":54.061,"KA2":52.959,"KB":61.607,"KB1":61.282,"KB2":62.946,"LA1":7.654,"LB1":8.708,"LB2":9.047,"LG1":10.142,"LG2":10.460,"LG3":10.511,"LG4":10.843,"LL":6.753},
             "HF":{"KA":55.382,"KA1":55.781,"KA2":54.579,"KB":63.562,"KB1":63.209,"KB2":64.936,"LA1":7.898,"LB1":9.021,"LB2":9.346,"LG1":10.514,"LG2":10.834,"LG3":10.891,"LG4":11.233,"LL":6.960},
             "TA":{"KA":57.106,"KA1":57.523,"KA2":56.270,"KB":65.556,"KB1":65.210,"KB2":66.999,"LA1":8.145,"LB1":9.342,"LB2":9.650,"LG1":10.892,"LG2":11.217,"LG3":11.278,"LG4":11.645,"LL":7.173},
             "W":{"KA":58.864,"KA1":59.308,"KA2":57.973,"KB":67.586,"KB1":67.233,"KB2":69.090,"LA1":8.396,"LB1":9.671,"LB2":9.960,"LG1":11.283,"LG2":11.608,"LG3":11.674,"LG4":12.063,"LL":7.388},
             "RE":{"KA":60.655,"KA1":61.130,"KA2":59.707,"KB":69.659,"KB1":69.296,"KB2":71.220,"LA1":8.651,"LB1":10.008,"LB2":10.273,"LG1":11.684,"LG2":12.010,"LG3":12.082,"LG4":12.492,"LL":7.604},
             "OS":{"KA":62.482,"KA1":62.990,"KA2":61.477,"KB":71.775,"KB1":71.404,"KB2":73.393,"LA1":8.910,"LB1":10.354,"LB2":10.597,"LG1":12.094,"LG2":12.422,"LG3":12.500,"LG4":12.923,"LL":7.822},
             "IR":{"KA":64.346,"KA1":64.885,"KA2":63.278,"KB":73.933,"KB1":73.549,"KB2":75.605,"LA1":9.174,"LB1":10.706,"LB2":10.919,"LG1":12.509,"LG2":12.842,"LG3":12.924,"LG4":13.368,"LL":8.046},
             "PT":{"KA":66.246,"KA1":66.821,"KA2":65.111,"KB":76.131,"KB1":75.736,"KB2":77.866,"LA1":9.441,"LB1":11.069,"LB2":11.249,"LG1":12.939,"LG2":13.270,"LG3":13.361,"LG4":13.828,"LL":8.268},
             "AU":{"KA":68.185,"KA1":68.792,"KA2":66.980,"KB":78.372,"KB1":77.968,"KB2":80.165,"LA1":9.712,"LB1":11.440,"LB2":11.583,"LG1":13.379,"LG2":13.710,"LG3":13.809,"LG4":14.300,"LL":8.494},
             "HG":{"KA":70.160,"KA1":70.807,"KA2":68.894,"KB":80.656,"KB1":80.258,"KB2":82.526,"LA1":9.987,"LB1":11.821,"LB2":11.922,"LG1":13.828,"LG2":14.162,"LG3":14.265,"LG4":14.778,"LL":8.721},
             "TL":{"KA":72.176,"KA1":72.859,"KA2":70.820,"KB":82.985,"KB1":82.558,"KB2":84.904,"LA1":10.267,"LB1":12.211,"LB2":12.270,"LG1":14.288,"LG2":14.625,"LG3":14.737,"LG4":15.272,"LL":8.953},
             "PB":{"KA":74.228,"KA1":74.956,"KA2":72.794,"KB":85.357,"KB1":84.922,"KB2":87.343,"LA1":10.550,"LB1":12.612,"LB2":12.621,"LG1":14.762,"LG2":15.101,"LG3":15.218,"LG4":15.777,"LL":9.185},
             "BI":{"KA":76.321,"KA1":77.095,"KA2":74.805,"KB":87.774,"KB1":87.335,"KB2":89.833,"LA1":10.837,"LB1":13.021,"LB2":12.978,"LG1":15.244,"LG2":15.582,"LG3":15.710,"LG4":16.295,"LL":9.420},
             "PO":{"KA":78.460,"KA1":79.279,"KA2":76.868,"KB":90.243,"KB1":89.809,"KB2":92.386,"LA1":11.129,"LB1":13.445,"LB2":13.338,"LG1":15.740,"LG2":16.070,"LG3":0.000,"LG4":0.000,"LL":9.664},
             "AT":{"KA":80.636,"KA1":81.499,"KA2":78.956,"KB":92.754,"KB1":92.319,"KB2":94.976,"LA1":11.425,"LB1":13.874,"LB2":13.705,"LG1":16.248,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "RN":{"KA":82.855,"KA1":83.768,"KA2":81.080,"KB":95.315,"KB1":94.877,"KB2":97.615,"LA1":11.725,"LB1":14.313,"LB2":14.077,"LG1":16.768,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "FR":{"KA":85.124,"KA1":86.089,"KA2":83.243,"KB":97.930,"KB1":97.483,"KB2":100.305,"LA1":12.029,"LB1":14.768,"LB2":14.448,"LG1":17.301,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "RA":{"KA":87.437,"KA1":88.454,"KA2":85.446,"KB":100.523,"KB1":100.136,"KB2":103.048,"LA1":12.338,"LB1":15.233,"LB2":14.839,"LG1":17.845,"LG2":18.179,"LG3":18.357,"LG4":19.084,"LL":10.622},
             "AC":{"KA":89.790,"KA1":90.868,"KA2":87.861,"KB":103.310,"KB1":102.846,"KB2":105.838,"LA1":12.650,"LB1":15.710,"LB2":15.227,"LG1":18.405,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "TH":{"KA":92.190,"KA1":93.334,"KA2":89.942,"KB":106.077,"KB1":105.592,"KB2":108.671,"LA1":12.967,"LB1":16.199,"LB2":15.621,"LG1":18.977,"LG2":19.305,"LG3":19.507,"LG4":20.292,"LL":11.119},
             "PA":{"KA":94.643,"KA1":95.852,"KA2":92.271,"KB":108.906,"KB1":108.408,"KB2":111.575,"LA1":13.288,"LB1":16.699,"LB2":16.022,"LG1":19.559,"LG2":19.872,"LG3":20.098,"LG4":20.882,"LL":11.366},
             "U":{"KA":97.143,"KA1":98.422,"KA2":94.649,"KB":111.786,"KB1":111.289,"KB2":114.549,"LA1":13.612,"LB1":17.217,"LB2":16.425,"LG1":20.163,"LG2":20.485,"LG3":20.713,"LG4":21.562,"LL":11.618},
             "NP":{"KA":99.693,"KA1":101.005,"KA2":97.023,"KB":114.720,"KB1":114.181,"KB2":117.533,"LA1":13.942,"LB1":17.747,"LB2":16.837,"LG1":20.774,"LG2":21.110,"LG3":21.340,"LG4":22.200,"LL":11.890},
             "PU":{"KA":102.295,"KA1":103.653,"KA2":99.457,"KB":117.716,"KB1":117.146,"KB2":120.592,"LA1":14.276,"LB1":18.291,"LB2":17.252,"LG1":21.401,"LG2":21.725,"LG3":21.982,"LG4":22.891,"LL":12.124},
             "AM":{"KA":104.952,"KA1":106.351,"KA2":101.932,"KB":120.775,"KB1":120.163,"KB2":123.706,"LA1":14.615,"LB1":18.849,"LB2":17.673,"LG1":22.042,"LG2":22.361,"LG3":0.000,"LG4":0.000,"LL":12.384},
             "CM":{"KA":107.670,"KA1":109.098,"KA2":104.448,"KB":123.903,"KB1":123.235,"KB2":126.875,"LA1":14.961,"LB1":19.393,"LB2":18.106,"LG1":22.699,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "BK":{"KA":110.450,"KA1":111.595,"KA2":107.023,"KB":127.102,"KB1":126.362,"KB2":130.101,"LA1":15.309,"LB1":19.971,"LB2":18.540,"LG1":23.370,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "CF":{"KA":113.298,"KA1":114.745,"KA2":109.603,"KB":130.377,"KB1":129.544,"KB2":133.383,"LA1":15.561,"LB1":20.562,"LB2":18.980,"LG1":24.056,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "ES":{"KA":116.217,"KA1":117.646,"KA2":112.244,"KB":133.730,"KB1":132.781,"KB2":136.724,"LA1":16.018,"LB1":21.166,"LB2":19.425,"LG1":24.758,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000},
             "FM":{"KA":119.210,"KA1":120.596,"KA2":114.926,"KB":137.167,"KB1":136.075,"KB2":140.122,"LA1":16.379,"LB1":21.785,"LB2":19.879,"LG1":25.475,"LG2":0.000,"LG3":0.000,"LG4":0.000,"LL":0.000}}
