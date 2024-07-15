tengo esta funcion
##
const sqlite3 = require('sqlite3').verbose();

  
  

class Database {

  constructor(databaseFile = 'mydatabase.db') {

    this.db = new sqlite3.Database(databaseFile);

  }

  
  

  async createTables() {

    try {

      await this.runQuery(`

        CREATE TABLE IF NOT EXISTS Facturas (

          idFactura INTEGER PRIMARY KEY AUTOINCREMENT,

          idEmpresa INTEGER NOT NULL,

          idTipoDocumento INTEGER NOT NULL,

          idCliente INTEGER NOT NULL,

          idFormaPago TEXT,

          idMetodoPago TEXT,

          Serie TEXT,

          Folio INTEGER,

          Fecha DATETIME NOT NULL,

          FechaSAT TEXT NOT NULL,

          SerieCertificado TEXT,

          Certificado TEXT,

          CadenaOriginal TEXT,

          CadenaOriginalTFD TEXT,

          SelloDigital TEXT,

          PorcentajeDescuento REAL NOT NULL,

          SubTotalAntesDescuento REAL NOT NULL,

          ImporteDescuento REAL NOT NULL,

          SubTotalConDescuento REAL,

          ImporteIVA REAL NOT NULL,

          Total REAL,

          DatosEnvio TEXT,

          Estatus TEXT NOT NULL,

          FechaCancelacion DATETIME,

          TotalLetras TEXT,

          ImporteIEPS REAL,

          ImporteRetIVA REAL,

          ImporteISR REAL,

          ImporteIMCD REAL,

          ImporteISSH REAL,

          RutaXML TEXT,

          UUID TEXT,

          SelloSAT TEXT,

          noCertificadoSAT TEXT,

          FechaTimbrado TEXT,

          CodigoBarras BLOB,

          Facturado BOOLEAN NOT NULL,

          idMoneda INTEGER NOT NULL,

          TipoCambio REAL NOT NULL,

          idUsuario INTEGER,

          NumCtaPago TEXT,

          FolioFiscalOrig TEXT,

          SerieFolioFiscalOrig TEXT,

          FechaFolioFiscalOrig TEXT,

          MontoFolioFiscalOrig REAL,

          Propina REAL,

          idCondicionesPago INTEGER,

          idEmpresaFolio INTEGER,

          AutoUnidad TEXT,

          AutoMarca TEXT,

          AutoModelo TEXT,

          AutoPlacas TEXT,

          AutoSiniestro TEXT,

          AutoPoliza TEXT,

          AutoReporte TEXT,

          LlavePrivada TEXT,

          RutaCertificado TEXT,

          idPac INTEGER,

          idNotaVenta INTEGER,

          MotivoCancelacion TEXT,

          Costo REAL,

          NotariaEscritura TEXT,

          DescripcionRetencionUno TEXT,

          ImporteRetencionUno REAL,

          DescripcionRetencionDos TEXT,

          ImporteRetencionDos REAL,

          TasaRetencionUno REAL,

          TasaRetencionDos REAL,

          idVendedor INTEGER,

          TicketCobrado INTEGER,

          DescImpLocalTrasladado TEXT,

          usoCFDi TEXT,

          TipoRelacion TEXT,

          TipoComprobante TEXT,

          RFC_PAC TEXT,

          ObservacionesReceta TEXT,

          idProcesoTempladora INTEGER,

          idFacturaDividida INTEGER,

          esFacturaGlobal INTEGER,

          FechaVencimientoCredito DATETIME,

          idObra INTEGER,

          idUsuarioCancela INTEGER,

          AutoFactura INTEGER,

          FolioAutoFactura TEXT,

          idDevolucion INTEGER,

          ClaveCancelacion TEXT,

          FolioSustituye TEXT,

          Exportacion TEXT,

          GlobalPeriodicidad TEXT,

          GlobalMeses TEXT,

          GlobalAnno TEXT,

          CodIdentifForestal TEXT,

          OficioAutorizacion TEXT,

          RFN TEXT,

          app INTEGER,

          idAlmacen INTEGER,

          UtilizadoNotaCredito REAL,

          idFacturaRelacionada INTEGER

        )

      `);

      await this.runQuery(`

        CREATE TABLE IF NOT EXISTS Productos (

          idProducto INTEGER PRIMARY KEY AUTOINCREMENT,

          idEmpresa INTEGER NOT NULL,

          Identificador TEXT,

          Producto TEXT NOT NULL,

          Modelo TEXT,

          Precio REAL NOT NULL,

          PrecioConIva REAL,

          PrecioCompra REAL,

          PrecioMayorista REAL,

          idTipoProducto INTEGER NOT NULL,

          idUnidadMedida INTEGER,

          CodigoBarras BLOB,

          Existencia REAL NOT NULL,

          IEPS REAL,

          AplicaIVA INTEGER NOT NULL,

          Maximo REAL,

          Minimo REAL,

          idUsuario INTEGER,

          idMoneda INTEGER,

          PorcientoUtilidad REAL,

          Precio3 REAL,

          Precio4 REAL,

          Precio5 REAL,

          idAlmacen INTEGER NOT NULL,

          Imagen BLOB,

          FechaAlta DATETIME,

          isRetornable INTEGER,

          CantidadBotellas INTEGER,

          VentaIndividual INTEGER,

          CodigoDeBarras TEXT,

          PorcientoIEPS REAL,

          Estatus TEXT,

          CodigoProveedor TEXT,

          Lote TEXT,

          Serie TEXT,

          FechaCaducidad DATETIME,

          Producto2 TEXT,

          idTipoProductoDetalle INTEGER,

          ClaveProdServ TEXT,

          PorcentajeDescuento REAL,

          Precio6 REAL,

          Precio7 REAL,

          Precio8 REAL,

          Precio9 REAL,

          Precio10 REAL,

          Precio11 REAL,

          Precio12 REAL,

          Precio13 REAL,

          Precio14 REAL,

          Precio15 REAL,

          Precio16 REAL,

          Precio17 REAL,

          Precio18 REAL,

          Precio19 REAL,

          Precio20 REAL,

          RequiereReceta INTEGER,

          TienePredial INTEGER,

          Pedimento TEXT,

          PorcentajePrecio2 REAL,

          PorcentajePrecio3 REAL,

          PorcentajePrecio4 REAL,

          PorcentajePrecio5 REAL,

          PorcentajePrecio6 REAL,

          PorcentajePrecio7 REAL,

          PorcentajePrecio8 REAL,

          PorcentajePrecio9 REAL,

          PorcentajePrecio10 REAL,

          PorcentajePrecio11 REAL,

          PorcentajePrecio12 REAL,

          PorcentajePrecio13 REAL,

          PorcentajePrecio14 REAL,

          PorcentajePrecio15 REAL,

          PorcentajePrecio16 REAL,

          PorcentajePrecio17 REAL,

          PorcentajePrecio18 REAL,

          PorcentajePrecio19 REAL,

          PorcentajePrecio20 REAL,

          Facturable INTEGER,

          CostoActual REAL,

          UnidadConversion REAL,

          UbicacionDescripcion TEXT,

          UbicacionPasillo TEXT,

          UbicacionFila TEXT,

          UbicacionNivel TEXT,

          PorcentajeComision REAL,

          ImporteComision REAL,

          Utilidad REAL,

          Peso REAL,

          Puntos INTEGER,

          idComplementoSAT INTEGER,

          EC_eCommerce INTEGER,

          PaqueteVirtual INTEGER,

          idPresentacion INTEGER,

          imagen2 BLOB,

          imagen3 BLOB,

          imagen4 BLOB,

          imagen5 BLOB,

          app INTEGER,

          todosLosClientes INTEGER,

          tiempoEntregaProv INTEGER,

          ajusteCiclo REAL

        )

      `);

      await this.runQuery(`

        CREATE TABLE IF NOT EXISTS FacturasDetalle (

          idFacturaDetalle INTEGER PRIMARY KEY AUTOINCREMENT,

          idFactura INTEGER NOT NULL,

          idProducto INTEGER NOT NULL,

          Cantidad REAL NOT NULL,

          PrecioInicial REAL NOT NULL,

          PrecioFinal REAL NOT NULL,

          SubTotalSinDescuentoDetalle REAL,

          PorcentajeDescuento REAL NOT NULL,

          SubTotalConDescuentoDetalle REAL,

          ImporteIVA REAL NOT NULL,

          IEPS REAL,

          RetIVA REAL,

          ISR REAL,

          IMCD REAL,

          ISSH REAL,

          TotalDetalle REAL,

          Observaciones TEXT,

          nombreAlumno TEXT,

          CURP TEXT,

          nivelEducativo TEXT,

          autRVOE TEXT,

          ComplementoAduana TEXT,

          ComplementoFechaPedimento TEXT,

          ComplementoPedimento TEXT,

          Devuelto REAL,

          CuentaPredial TEXT,

          ExistenciaFinal REAL,

          idProductoSeries TEXT,

          PorcientoIEPS REAL,

          idProductoLotes TEXT,

          DescImpLocalTrasladado TEXT,

          Tara REAL,

          PorcientoIVA REAL,

          PorcientoRetIVA REAL,

          PorcientoISR REAL,

          Exento INTEGER,

          idProductoTallas TEXT,

          esPaquete INTEGER,

          DescuentoDetalle REAL,

          IdentificadorProducto TEXT,

          FechaInicialContrato DATETIME,

          FechaFinalContrato DATETIME,

          FactorExistencia REAL,

          DescripcionProducto TEXT,

          idMotivoDescuento INTEGER,

          Placas TEXT,

          FolioHolograma INTEGER,

          PrecioCompra REAL,

          PorcentajeDescuento1 REAL,

          DescuentoDetalle1 REAL,

          RfcACuentaTerceros TEXT,

          NombreACuentaTerceros TEXT,

          RegimenFiscalACuentaTerceros TEXT,

          DomicilioFiscalACuentaTerceros TEXT,

          idFacturaDevolucion INTEGER,

          AnualidadContrato REAL,

          idPedidoCliente INTEGER,

          Surtido REAL

        )

      `);

  

      console.log('Tables created successfully!');

    } catch (error) {

      console.error('Error creating tables:', error);

    }

  }

  

  async runQuery(query, params = []) {

    return new Promise((resolve, reject) => {

      this.db.run(query, params, (err) => {

        if (err) {

          reject(err);

        } else {

          resolve();

        }

      });

    });

  }

  

  async getAll(tableName) {

    return new Promise((resolve, reject) => {

      this.db.all(`SELECT * FROM ${tableName}`, (err, rows) => {

        if (err) {

          reject(err);

        } else {

          resolve(rows);

        }

      });

    });

  }

  

  async getOne(tableName, whereClause, params = []) {

    return new Promise((resolve, reject) => {

      this.db.get(`SELECT * FROM ${tableName} WHERE ${whereClause}`, params, (err, row) => {

        if (err) {

          reject(err);

        } else {

          resolve(row);

        }

      });

    });

  }

  

  async insert(tableName, data) {

    const columns = Object.keys(data).join(',');

    const placeholders = Object.keys(data).map(() => '?').join(',');

    const values = Object.values(data);

  

    return new Promise((resolve, reject) => {

      this.db.run(

        `INSERT INTO ${tableName} (${columns}) VALUES (${placeholders})`,

        values,

        (err, result) => {

          if (err) {

            reject(err);

          } else {

            resolve(result.lastID);

          }

        }

      );

    });

  }

  

  async update(tableName, data, whereClause, params = []) {

    const setClause = Object.entries(data)

      .map(([key, value]) => `${key} = ?`)

      .join(',');

    const values = [...Object.values(data), ...params];

  

    return new Promise((resolve, reject) => {

      this.db.run(

        `UPDATE ${tableName} SET ${setClause} WHERE ${whereClause}`,

        values,

        (err) => {

          if (err) {

            reject(err);

          } else {

            resolve();

          }

        }

      );

    });

  }

  

  async delete(tableName, whereClause, params = []) {

    return new Promise((resolve, reject) => {

      this.db.run(

        `DELETE FROM ${tableName} WHERE ${whereClause}`,

        params,

        (err) => {

          if (err) {

            reject(err);

          } else {

            resolve();

          }

        }

      );

    });

  }

  

  close() {

    this.db.close();

  }

}

  
  

const db = new Database('eFactDCS_CFDi.db');

  

db.createTables();

  

module.exports = Database;

tengo este quiero modificar para que utilice mi classe de base de datos 
## 
import React, { useState, useEffect } from 'react';

import { View, Text, FlatList, Button } from 'react-native';

import SQLite from 'react-native-sqlite-storage';

  

const db = SQLite.openDatabase({ name: 'eFactDCS_CFDi.db', createFromLocation: '~eFactDCS_CFDi.db' });

  

const xd = () => {

  const [products, setProducts] = useState([]);

  const [isLoading, setIsLoading] = useState(true);

  

  useEffect(() => {

    fetchProducts();

  }, []);

  

  const fetchProducts = async () => {

    setIsLoading(true);

    try {

      const response = await fetch('http://localhost:8000/productos'); // Reemplaza con tu endpoint

      const data = await response.json();

      setProducts(data);

    } catch (error) {

      console.error('Error fetching products:', error);

    } finally {

      setIsLoading(false);

    }

  };

  

  const saveProducts = async (products) => {

    await Promise.all(products.map(async (product) => {

      try {

        await db.transaction(async (tx) => {

          await tx.executeSql(

            'INSERT INTO Productos (idEmpresa, Identificador, Producto, Modelo, Precio, PrecioConIva, PrecioCompra, PrecioMayorista, idTipoProducto, idUnidadMedida, CodigoBarras, Existencia, IEPS, AplicaIVA, Maximo, Minimo, idUsuario, idMoneda, PorcientoUtilidad, Precio3, Precio4, Precio5, idAlmacen, Imagen, FechaAlta, isRetornable, CantidadBotellas, VentaIndividual, CodigoDeBarras, PorcientoIEPS, Estatus, CodigoProveedor, Lote, Serie, FechaCaducidad, Producto2, idTipoProductoDetalle, ClaveProdServ, PorcentajeDescuento, Precio6, Precio7, Precio8, Precio9, Precio10, Precio11, Precio12, Precio13, Precio14, Precio15, Precio16, Precio17, Precio18, Precio19, Precio20, RequiereReceta, TienePredial, Pedimento, PorcentajePrecio2, PorcentajePrecio3, PorcentajePrecio4, PorcentajePrecio5, PorcentajePrecio6, PorcentajePrecio7, PorcentajePrecio8, PorcentajePrecio9, PorcentajePrecio10, PorcentajePrecio11, PorcentajePrecio12, PorcentajePrecio13, PorcentajePrecio14, PorcentajePrecio15, PorcentajePrecio16, PorcentajePrecio17, PorcentajePrecio18, PorcentajePrecio19, PorcentajePrecio20, Facturable, CostoActual, UnidadConversion, UbicacionDescripcion, UbicacionPasillo, UbicacionFila, UbicacionNivel, PorcentajeComision, ImporteComision, Utilidad, Peso, Puntos, idComplementoSAT, EC_eCommerce, PaqueteVirtual, idPresentacion, imagen2, imagen3, imagen4, imagen5, app, todosLosClientes, tiempoEntregaProv, ajusteCiclo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',

            [

              product.idEmpresa,

              product.Identificador,

              product.Producto,

              product.Modelo,

              product.Precio,

              product.PrecioConIva,

              product.PrecioCompra,

              product.PrecioMayorista,

              product.idTipoProducto,

              product.idUnidadMedida,

              product.CodigoBarras,

              product.Existencia,

              product.IEPS,

              product.AplicaIVA,

              product.Maximo,

              product.Minimo,

              product.idUsuario,

              product.idMoneda,

              product.PorcientoUtilidad,

              product.Precio3,

              product.Precio4,

              product.Precio5,

              product.idAlmacen,

              product.Imagen,

              product.FechaAlta,

              product.isRetornable,

              product.CantidadBotellas,

              product.VentaIndividual,

              product.CodigoDeBarras,

              product.PorcientoIEPS,

              product.Estatus,

              product.CodigoProveedor,

              product.Lote,

              product.Serie,

              product.FechaCaducidad,

              product.Producto2,

              product.idTipoProductoDetalle,

              product.ClaveProdServ,

              product.PorcentajeDescuento,

              product.Precio6,

              product.Precio7,

              product.Precio8,

              product.Precio9,

              product.Precio10,

              product.Precio11,

              product.Precio12,

              product.Precio13,

              product.Precio14,

              product.Precio15,

              product.Precio16,

              product.Precio17,

              product.Precio18,

              product.Precio19,

              product.Precio20,

              product.RequiereReceta,

              product.TienePredial,

              product.Pedimento,

              product.PorcentajePrecio2,

              product.PorcentajePrecio3,

              product.PorcentajePrecio4,

              product.PorcentajePrecio5,

              product.PorcentajePrecio6,

              product.PorcentajePrecio7,

              product.PorcentajePrecio8,

              product.PorcentajePrecio9,

              product.PorcentajePrecio10,

              product.PorcentajePrecio11,

              product.PorcentajePrecio12,

              product.PorcentajePrecio13,

              product.PorcentajePrecio14,

              product.PorcentajePrecio15,

              product.PorcentajePrecio16,

              product.PorcentajePrecio17,

              product.PorcentajePrecio18,

              product.PorcentajePrecio19,

              product.PorcentajePrecio20,

              product.Facturable,

              product.CostoActual,

              product.UnidadConversion,

              product.UbicacionDescripcion,

              product.UbicacionPasillo,

              product.UbicacionFila,

              product.UbicacionNivel,

              product.PorcentajeComision,

              product.ImporteComision,

              product.Utilidad,

              product.Peso,

              product.Puntos,

              product.idComplementoSAT,

              product.EC_eCommerce,

              product.PaqueteVirtual,

              product.idPresentacion,

              product.imagen2,

              product.imagen3,

              product.imagen4,

              product.imagen5,

              product.app,

              product.todosLosClientes,

              product.tiempoEntregaProv,

              product.ajusteCiclo

            ]

          );

        });

      } catch (error) {

        console.error('Error inserting product:', error);

      }

    }));

  };

  

  const renderItem = ({ item }) => (

    <View style={{ padding: 10, borderBottomWidth: 1, borderBottomColor: '#ddd' }}>

      <Text>Producto: {item.Producto}</Text>

      <Text>Precio: {item.Precio}</Text>

    </View>

  );

  

  return (

    <View style={{ flex: 1, padding: 20 }}>

      <Text style={{ fontSize: 20, marginBottom: 20 }}>Productos</Text>

      {isLoading ? (

        <Text>Cargando...</Text>

      ) : (

        <FlatList

          data={products}

          renderItem={renderItem}

          keyExtractor={(item) => item.idProducto.toString()}

        />

      )}

      <Button title="Guardar Productos" onPress={() => saveProducts(products)} />

    </View>

  );

};

  

export default xd;


me ayudas a implementarlo porfavor 
