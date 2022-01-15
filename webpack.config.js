const path = require('path');
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const TerserJSPlugin = require('terser-webpack-plugin');
const { VueLoaderPlugin } = require('vue-loader')
const webpack = require('webpack');

module.exports = (_env, options) => {
  if (!('VUE_DEVTOOLS' in process.env) || process.env.VUE_DEVTOOLS.length === 0) {
    process.env.VUE_DEVTOOLS = options.mode;
  }

  const config = {

    context: __dirname,

    // MARK: Specify the 'entry point' js for the vue application. Multiple entry points can be
    // declared using an object
    entry: {
      main: './mdot_vue/main.js'
    },

    optimization: {
      minimizer: [new TerserJSPlugin({})],
      splitChunks: {
        chunks: 'all',
      },
    },

    // MARK: Put the 'bundles' in a name-spaced directory in the django app statics
    // where it be collected when using 'collectstatic'
    output: {
      path: path.resolve('./mdot/static/mdot/bundles/'),
      filename: "[name]-[contenthash].js",
      publicPath: '/static/mdot/bundles/',
    },

    plugins: [
      new webpack.EnvironmentPlugin(['VUE_DEVTOOLS']),
      new webpack.DefinePlugin({
        __VUE_OPTIONS_API__: true,
        __VUE_PROD_DEVTOOLS__: false,
      }),
      new CleanWebpackPlugin(),
      new VueLoaderPlugin(),
      new MiniCssExtractPlugin({
        filename: "[name]-[contenthash].css",
      }),

      // MARK: Put the 'webpack-stats.json' file in the static location directory so that it 
      // can be accessed during development and production static collection
      new BundleTracker({
        filename: './mdot/static/webpack-stats.json'
      }),
    ],

    module: {
      rules: [
        {
          test: /\.vue$/,
          loader: 'vue-loader'
        },
        {
          test: /\.m?js$/,
          exclude: /(node_modules|bower_components)/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: [
                [
                  '@babel/preset-env',
                  {
                    'useBuiltIns': 'entry',
                    'corejs': 3,
                  }
                ],
              ]
            }
          }
        },
        {
          test: /\.s[ac]ss$/,
          use: [MiniCssExtractPlugin.loader, "css-loader", "sass-loader"]
        },
        {
          test: /\.css$/,
          use: [MiniCssExtractPlugin.loader, "css-loader"]
        },
        {
          test: /\.(png|jpe?g|gif)$/i,
          type: 'asset/resource',
        },
      ]
    },

    resolve: {
      extensions: ['.js', '.vue'],
      alias: {
        'Vue': 'vue/dist/vue.esm-bundler.js',
      }
    }
  };

  if (process.env.BUNDLE_ANALYZER === "True") {
    config.plugins.push(
      new BundleAnalyzerPlugin({
        analyzerHost: '0.0.0.0',
      })
    );
  }

  return config;
}