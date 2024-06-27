
funciones
- Traer datos de back4app divididos con su respectiva columna
	



# Tareas, ideas y aprendizaje

## Explicación 
Tengo 2 tablas en mi base de datos en back4app una de ellas llamada

## Tipo de datos de las tablas en back4app 
[

  {

    "className": "_User",

    "fields": {

      "objectId": {

        "type": "String"

      },

      "createdAt": {

        "type": "Date"

      },

      "updatedAt": {

        "type": "Date"

      },

      "ACL": {

        "type": "ACL"

      },

      "username": {

        "type": "String"

      },

      "password": {

        "type": "String"

      },

      "email": {

        "type": "String"

      },

      "emailVerified": {

        "type": "Boolean"

      },

      "authData": {

        "type": "Object"

      }

    },

    "classLevelPermissions": {

      "find": {

        "*": true

      },

      "get": {

        "*": true

      },

      "count": {

        "*": true

      },

      "create": {

        "*": true

      },

      "update": {

        "*": true

      },

      "delete": {

        "*": true

      },

      "addField": {

        "*": true

      },

      "protectedFields": {

        "*": []

      }

    }

  },

  {

    "className": "_Role",

    "fields": {

      "objectId": {

        "type": "String"

      },

      "createdAt": {

        "type": "Date"

      },

      "updatedAt": {

        "type": "Date"

      },

      "ACL": {

        "type": "ACL"

      },

      "name": {

        "type": "String"

      },

      "users": {

        "type": "Relation",

        "targetClass": "_User"

      },

      "roles": {

        "type": "Relation",

        "targetClass": "_Role"

      }

    },

    "classLevelPermissions": {

      "find": {

        "*": true

      },

      "get": {

        "*": true

      },

      "count": {

        "*": true

      },

      "create": {

        "*": true

      },

      "update": {

        "*": true

      },

      "delete": {

        "*": true

      },

      "addField": {

        "*": true

      },

      "protectedFields": {

        "*": []

      }

    }

  },

  {

    "className": "B4aVehicle",

    "fields": {

      "objectId": {

        "type": "String"

      },

      "createdAt": {

        "type": "Date"

      },

      "updatedAt": {

        "type": "Date"

      },

      "ACL": {

        "type": "ACL"

      },

      "name": {

        "type": "String"

      },

      "color": {

        "type": "String"

      },

      "price": {

        "type": "Number"

      }

    },

    "classLevelPermissions": {

      "find": {

        "*": true

      },

      "get": {

        "*": true

      },

      "count": {

        "*": true

      },

      "create": {

        "*": true

      },

      "update": {

        "*": true

      },

      "delete": {

        "*": true

      },

      "addField": {

        "*": true

      },

      "protectedFields": {

        "*": []

      }

    }

  },

  {

    "className": "Producto",

    "fields": {

      "objectId": {

        "type": "String"

      },

      "createdAt": {

        "type": "Date"

      },

      "updatedAt": {

        "type": "Date"

      },

      "ACL": {

        "type": "ACL"

      },

      "app": {

        "type": "Number"

      },

      "IEPS": {

        "type": "Number"

      },

      "Peso": {

        "type": "Number"

      },

      "Imagen": {

        "type": "Object"

      },

      "Maximo": {

        "type": "Number"

      },

      "Minimo": {

        "type": "Number"

      },

      "Modelo": {

        "type": "String"

      },

      "Precio": {

        "type": "Number"

      },

      "Puntos": {

        "type": "Number"

      },

      "Estatus": {

        "type": "String"

      },

      "Precio3": {

        "type": "Number"

      },

      "Precio4": {

        "type": "Number"

      },

      "Precio5": {

        "type": "Number"

      },

      "Precio6": {

        "type": "Number"

      },

      "Precio7": {

        "type": "Number"

      },

      "Precio8": {

        "type": "Number"

      },

      "Precio9": {

        "type": "Number"

      },

      "imagen2": {

        "type": "Object"

      },

      "imagen3": {

        "type": "Object"

      },

      "imagen4": {

        "type": "Object"

      },

      "imagen5": {

        "type": "Object"

      },

      "Precio10": {

        "type": "Number"

      },

      "Precio11": {

        "type": "Number"

      },

      "Precio12": {

        "type": "Number"

      },

      "Precio13": {

        "type": "Number"

      },

      "Precio14": {

        "type": "Number"

      },

      "Precio15": {

        "type": "Number"

      },

      "Precio16": {

        "type": "Number"

      },

      "Precio17": {

        "type": "Number"

      },

      "Precio18": {

        "type": "Number"

      },

      "Precio19": {

        "type": "Number"

      },

      "Precio20": {

        "type": "Number"

      },

      "Producto": {

        "type": "String"

      },

      "Utilidad": {

        "type": "Number"

      },

      "idMoneda": {

        "type": "Number"

      },

      "AplicaIVA": {

        "type": "Number"

      },

      "FechaAlta": {

        "type": "String"

      },

      "Producto2": {

        "type": "String"

      },

      "idAlmacen": {

        "type": "Number"

      },

      "idEmpresa": {

        "type": "Number"

      },

      "idUsuario": {

        "type": "Number"

      },

      "Existencia": {

        "type": "Number"

      },

      "Facturable": {

        "type": "Number"

      },

      "idProducto": {

        "type": "Number"

      },

      "CostoActual": {

        "type": "Number"

      },

      "CodigoBarras": {

        "type": "Object"

      },

      "EC_eCommerce": {

        "type": "Number"

      },

      "PrecioCompra": {

        "type": "Number"

      },

      "PrecioConIva": {

        "type": "Number"

      },

      "TienePredial": {

        "type": "Number"

      },

      "isRetornable": {

        "type": "Number"

      },

      "ClaveProdServ": {

        "type": "String"

      },

      "Identificador": {

        "type": "String"

      },

      "PorcientoIEPS": {

        "type": "Number"

      },

      "CodigoDeBarras": {

        "type": "String"

      },

      "FechaCaducidad": {

        "type": "String"

      },

      "PaqueteVirtual": {

        "type": "Number"

      },

      "RequiereReceta": {

        "type": "Number"

      },

      "idPresentacion": {

        "type": "Number"

      },

      "idTipoProducto": {

        "type": "Number"

      },

      "idUnidadMedida": {

        "type": "Number"

      },

      "CodigoProveedor": {

        "type": "String"

      },

      "ImporteComision": {

        "type": "Number"

      },

      "PrecioMayorista": {

        "type": "Number"

      },

      "VentaIndividual": {

        "type": "Number"

      },

      "CantidadBotellas": {

        "type": "Number"

      },

      "UnidadConversion": {

        "type": "Number"

      },

      "idComplementoSAT": {

        "type": "Number"

      },

      "PorcentajePrecio2": {

        "type": "Number"

      },

      "PorcentajePrecio3": {

        "type": "Number"

      },

      "PorcentajePrecio4": {

        "type": "Number"

      },

      "PorcentajePrecio5": {

        "type": "Number"

      },

      "PorcentajePrecio6": {

        "type": "Number"

      },

      "PorcentajePrecio7": {

        "type": "Number"

      },

      "PorcentajePrecio8": {

        "type": "Number"

      },

      "PorcentajePrecio9": {

        "type": "Number"

      },

      "PorcientoUtilidad": {

        "type": "Number"

      },

      "PorcentajeComision": {

        "type": "Number"

      },

      "PorcentajePrecio10": {

        "type": "Number"

      },

      "PorcentajePrecio11": {

        "type": "Number"

      },

      "PorcentajePrecio12": {

        "type": "Number"

      },

      "PorcentajePrecio13": {

        "type": "Number"

      },

      "PorcentajePrecio14": {

        "type": "Number"

      },

      "PorcentajePrecio15": {

        "type": "Number"

      },

      "PorcentajePrecio16": {

        "type": "Number"

      },

      "PorcentajePrecio17": {

        "type": "Number"

      },

      "PorcentajePrecio18": {

        "type": "Number"

      },

      "PorcentajePrecio19": {

        "type": "Number"

      },

      "PorcentajePrecio20": {

        "type": "Number"

      },

      "PorcentajeDescuento": {

        "type": "Number"

      },

      "idTipoProductoDetalle": {

        "type": "Number"

      }

    },

    "classLevelPermissions": {

      "find": {

        "*": true

      },

      "get": {

        "*": true

      },

      "count": {

        "*": true

      },

      "create": {

        "*": true

      },

      "update": {

        "*": true

      },

      "delete": {

        "*": true

      },

      "addField": {

        "*": true

      },

      "protectedFields": {

        "*": []

      }

    }

  },

  {

    "className": "Cliente",

    "fields": {

      "objectId": {

        "type": "String"

      },

      "createdAt": {

        "type": "Date"

      },

      "updatedAt": {

        "type": "Date"

      },

      "ACL": {

        "type": "ACL"

      },

      "RFC": {

        "type": "String"

      },

      "app": {

        "type": "Number"

      },

      "Pais": {

        "type": "String"

      },

      "Calle": {

        "type": "String"

      },

      "email": {

        "type": "String"

      },

      "Estado": {

        "type": "String"

      },

      "Nombre": {

        "type": "String"

      },

      "Colonia": {

        "type": "String"

      },

      "Estatus": {

        "type": "String"

      },

      "idCanal": {

        "type": "Number"

      },

      "usoCFDi": {

        "type": "String"

      },

      "Contacto": {

        "type": "String"

      },

      "ClavePais": {

        "type": "String"

      },

      "FechaAlta": {

        "type": "String"

      },

      "Localidad": {

        "type": "String"

      },

      "Municipio": {

        "type": "String"

      },

      "PaginaWeb": {

        "type": "String"

      },

      "Telefonos": {

        "type": "String"

      },

      "idCliente": {

        "type": "Number"

      },

      "idEmpresa": {

        "type": "Number"

      },

      "idUsuario": {

        "type": "Number"

      },

      "GesemCloud": {

        "type": "Number"

      },

      "NumCtaPago": {

        "type": "String"

      },

      "Referencia": {

        "type": "String"

      },

      "SistemaWeb": {

        "type": "Number"

      },

      "ClaveEstado": {

        "type": "String"

      },

      "DiasCredito": {

        "type": "Number"

      },

      "idFormaPago": {

        "type": "String"

      },

      "isMayorista": {

        "type": "Number"

      },

      "CodigoPostal": {

        "type": "String"

      },

      "idMetodoPago": {

        "type": "String"

      },

      "CodigoCliente": {

        "type": "String"

      },

      "Identificador": {

        "type": "String"

      },

      "LimiteCredito": {

        "type": "Number"

      },

      "idClienteZona": {

        "type": "Number"

      },

      "CuentaContable": {

        "type": "String"

      },

      "NumeroExterior": {

        "type": "String"

      },

      "NumeroInterior": {

        "type": "String"

      },

      "RegimenCapital": {

        "type": "String"

      },

      "SistemaGestion": {

        "type": "Number"

      },

      "idComisionista": {

        "type": "Number"

      },

      "SistemaPtoVenta": {

        "type": "Number"

      },

      "idComisionista2": {

        "type": "Number"

      },

      "idGiroComercial": {

        "type": "Number"

      },

      "DireccionEntrega": {

        "type": "String"

      },

      "SistemaEscritorio": {

        "type": "Number"

      },

      "idClienteZonaRuta": {

        "type": "Number"

      },

      "idCondicionesPago": {

        "type": "Number"

      },

      "PorcentajeDescuento": {

        "type": "Number"

      },

      "ObservacionesCliente": {

        "type": "String"

      },

      "RegimenFiscalReceptor": {

        "type": "String"

      }

    },

    "classLevelPermissions": {

      "find": {

        "*": true

      },

      "get": {

        "*": true

      },

      "count": {

        "*": true

      },

      "create": {

        "*": true

      },

      "update": {

        "*": true

      },

      "delete": {

        "*": true

      },

      "addField": {

        "*": true

      },

      "protectedFields": {

        "*": []

      }

    }

  },

  {

    "className": "Comisionista",

    "fields": {

      "objectId": {

        "type": "String"

      },

      "createdAt": {

        "type": "Date"

      },

      "updatedAt": {

        "type": "Date"

      },

      "ACL": {

        "type": "ACL"

      },

      "Meta": {

        "type": "Number"

      },

      "email": {

        "type": "String"

      },

      "Nombre": {

        "type": "String"

      },

      "Estatus": {

        "type": "String"

      },

      "idBanco": {

        "type": "Number"

      },

      "LiderUDN": {

        "type": "Number"

      },

      "Direccion": {

        "type": "String"

      },

      "Telefonos": {

        "type": "String"

      },

      "idEmpresa": {

        "type": "Number"

      },

      "idUsuario": {

        "type": "Number"

      },

      "Porcentaje": {

        "type": "Number"

      },

      "SueldoBase": {

        "type": "Number"

      },

      "idComisionista": {

        "type": "Number"

      },

      "CodigoComisionista": {

        "type": "String"

      },

      "idTipoComisionista": {

        "type": "Number"

      },

      "MunicipioComisionista": {

        "type": "String"

      },

      "ClaveEstadoComisionista": {

        "type": "String"

      },

      "PorcientoPagoComisiones": {

        "type": "Number"

      }

    },

    "classLevelPermissions": {

      "find": {

        "*": true

      },

      "get": {

        "*": true

      },

      "count": {

        "*": true

      },

      "create": {

        "*": true

      },

      "update": {

        "*": true

      },

      "delete": {

        "*": true

      },

      "addField": {

        "*": true

      },

      "protectedFields": {

        "*": []

      }

    }

  }

]

## Tipo de datos de mis tablas originales con las que servi back4app
PRODUCTOS[icon: airflow, color: orange] {
    idEmpresa FK, int(4), NOT NULL
    Identificador, varchar(50), NULL
    Producto, varchar(1000), NOT NULL
    Modelo, varchar(50), NULL
    Precio, numeric(9), NOT NULL
    PrecioConIva, numeric(9), NULL
    PrecioCompra, numeric(9), NULL
    PrecioMayorista, numeric(9), NULL
    idTipoProducto, int(4), NOT NULL
    idUnidadMedida, int(4), NULL
    CodigoBarras, image(16), NULL
    Existencia, numeric(9), NOT NULL
    IEPS, numeric(9), NULL
    AplicaIVA, smallint(2), NOT NULL
    Maximo, numeric(9), NULL
    Minimo, numeric(9), NULL
    idUsuario, int(4), NULL
    idMoneda, int(4), NULL
    PorcientoUtilidad, numeric(9), NULL
    Precio3, numeric(9), NULL
    Precio4, numeric(9), NULL
    Precio5, numeric(9), NULL
    idAlmacen, int(4), NOT NULL
    Imagen, image(16), NULL
    FechaAlta, datetime(8), NULL
    isRetornable, smallint(2), NULL
    CantidadBotellas, smallint(2), NULL
    VentaIndividual, smallint(2), NULL
    CodigoDeBarras, varchar(50), NULL
    PorcientoIEPS, numeric(9), NULL
    Estatus, char(1), NULL
    CodigoProveedor, varchar(100), NULL
    Lote, varchar(50), NULL
    Serie, varchar(50), NULL
    FechaCaducidad, datetime(8), NULL
    Producto2, varchar(500), NULL
    idTipoProductoDetalle, int(4), NULL
    ClaveProdServ, varchar(10), NULL
    PorcentajeDescuento, numeric(9), NULL
    Precio6, numeric(9), NULL
    Precio7, numeric(9), NULL
    Precio8, numeric(9), NULL
    Precio9, numeric(9), NULL
    Precio10, numeric(9), NULL
    Precio11, numeric(9), NULL
    Precio12, numeric(9), NULL
    Precio13, numeric(9), NULL
    Precio14, numeric(9), NULL
    Precio15, numeric(9), NULL
    Precio16, numeric(9), NULL
    Precio17, numeric(9), NULL
    Precio18, numeric(9), NULL
    Precio19, numeric(9), NULL
    Precio20, numeric(9), NULL
    RequiereReceta, smallint(2), NULL
    TienePredial, smallint(2), NULL
    Pedimento, varchar(200), NULL
    PorcentajePrecio2, numeric(9), NULL
    PorcentajePrecio3, numeric(9), NULL
    PorcentajePrecio4, numeric(9), NULL
    PorcentajePrecio5, numeric(9), NULL
    PorcentajePrecio6, numeric(9), NULL
    PorcentajePrecio7, numeric(9), NULL
    PorcentajePrecio8, numeric(9), NULL
    PorcentajePrecio9, numeric(9), NULL
    PorcentajePrecio10, numeric(9), NULL
    PorcentajePrecio11, numeric(9), NULL
    PorcentajePrecio12, numeric(9), NULL
    PorcentajePrecio13, numeric(9), NULL
    PorcentajePrecio14, numeric(9), NULL
    PorcentajePrecio15, numeric(9), NULL
    PorcentajePrecio16, numeric(9), NULL
    PorcentajePrecio17, numeric(9), NULL
    PorcentajePrecio18, numeric(9), NULL
    PorcentajePrecio19, numeric(9), NULL
    PorcentajePrecio20, numeric(9), NULL
    Facturable, int(4), NULL
    CostoActual, numeric(9), NULL
    UnidadConversion, numeric(9), NULL
    UbicacionDescripcion, varchar(500), NULL
    UbicacionPasillo, varchar(50), NULL
    UbicacionFila, varchar(50), NULL
    UbicacionNivel, varchar(50), NULL
    PorcentajeComision, numeric(9), NULL
    ImporteComision, numeric(9), NULL
    Utilidad, numeric(9), NULL
    Peso, numeric(9), NULL
    Puntos, int(4), NULL
    idComplementoSAT, int(4), NULL
    EC_eCommerce, int(4), NULL
    PaqueteVirtual, int(4), NULL
    idPresentacion, int(4), NULL
    imagen2, image(16), NULL
    imagen3, image(16), NULL
    imagen4, image(16), NULL
    imagen5, image(16), NULL
    app, int(4), NULL
    todosLosClientes, smallint(2), NULL
    tiempoEntregaProv, int(4), NULL
    ajusteCiclo, numeric(9), NULL
}
COMISIONISTA[icon: airflow, color: pink] {
    idEmpresa FK, int(4), NOT NULL
    idTipoComisionista, int(4), NULL
    CodigoComisionista, varchar(20), NULL
    Nombre, varchar(300), NOT NULL
    Telefonos, varchar(100), NOT NULL
    email, varchar(100), NOT NULL
    Porcentaje, numeric(9), NOT NULL
    Direccion, varchar(200), NULL
    idUsuario, int(4), NOT NULL
    idBanco, int(4), NULL
    NumeroCuenta, varchar(20), NULL
    CLABE, varchar(20), NULL
    Meta, numeric(9), NULL
    PorcientoPagoComisiones, numeric(9), NULL
    Estatus, char(1), NULL
    SueldoBase, numeric(9), NULL
    LiderUDN, int(4), NULL
    ClaveEstadoComisionista, char(3), NULL
    MunicipioComisionista, varchar(50), NULL
    FechaIngreso, datetime(8), NULL
}
CLIENTE[icon: airflow, color: orange] {
    idEmpresa FK, int(4), NOT NULL
    CodigoCliente, varchar(20), NOT NULL
    Nombre, varchar(300), NULL
    RFC, varchar(13), NOT NULL
    Calle, varchar(150), NULL
    NumeroExterior, varchar(50), NULL
    NumeroInterior, varchar(50), NULL
    Colonia, varchar(100), NULL
    Localidad, varchar(100), NULL
    Referencia, varchar(100), NULL
    Municipio, varchar(100), NULL
    Estado, varchar(100), NULL
    Pais, varchar(100), NULL
    CodigoPostal, char(6), NULL
    Contacto, varchar(100), NULL
    Telefonos, varchar(100), NULL
    email, varchar(1000), NULL
    PaginaWeb, varchar(100), NULL
    CuentaContable, varchar(20), NULL
    idUsuario, int(4), NULL
    NumCtaPago, varchar(60), NULL
    FechaAlta, datetime(8), NULL
    CodigoBarras, image(16), NULL
    idPAC, int(4), NULL
    idComisionista, int(4), NULL
    isMayorista, int(4), NULL
    Estatus, char(1), NULL
    DiasCredito, int(4), NULL
    LimiteCredito, numeric(9), NULL
    SistemaWeb, tinyint(1), NULL
    SistemaEscritorio, tinyint(1), NULL
    SistemaGestion, tinyint(1), NULL
    idComisionista2, int(4), NULL
    idGiroComercial, int(4), NULL
    PorcentajeDescuento, numeric(9), NULL
    ClaveEstado, varchar(3), NULL
    ClavePais, varchar(3), NULL
    NumRegIdTrib, varchar(40), NULL
    idFormaPago, varchar(10), NULL
    DireccionEntrega, varchar(500), NULL
    idCanal, int(4), NULL
    idMetodoPago, varchar(10), NULL
    idCondicionesPago, int(4), NULL
    usoCFDi, char(3), NULL
    SistemaPtoVenta, tinyint(1), NULL
    ObservacionesCliente, varchar(200), NULL
    CURP, varchar(18), NULL
    FechaNacimiento, datetime(8), NULL
    GesemCloud, tinyint(1), NULL
    Foto, image(16), NULL
    FechaProximoPago, datetime(8), NULL
    RegimenFiscalReceptor, char(3), NULL
    RegimenCapital, varchar(50), NULL
    CodIdentifForestal, varchar(20), NULL
    OficioAutorizacion, varchar(20), NULL
    RFN, varchar(20), NULL
    app, int(4), NULL
    Categoria, char(3), NULL
    Identificador, varchar(10), NULL
    idClienteZona, int(4), NULL
    idClienteZonaRuta, int(4), NULL
    idSucursal, int(4), NULL
}
## Credenciales back4app
App Management

These options will affect your entire app.

Parse API

Parse API configurations

Parse API Address

https://parseapi.back4app.com

Parse Version

4.5.0

Database

Database configurations

Show Database URI

postgres://tNSa9c4I3D:nzmgJZF5lMksPVbvkgFVSCgO@SharedPostgreSQL01A.back4app.com:5433/20261804962941a99622db66c29ace9d

App Keys

These are the unique identifiers used to access this app.

Application ID

Main ID that uniquely specifies this app.  
Used with one of the keys below.

T6eE4t3UVT4V3rNe7bONfdcDJIjCozXEY0OXW0b1

Client key

Use this in consumer clients, such as  
the iOS or Android SDKs.

gb0owxPpDWyhrJEWqMw4Jiowo3LvcD9N5GkeaXHl

JavaScript key

Use this when making requests from JavaScript clients.

465NkYCjdHAbbhUkoGYF1eM4RR7oBP2i1pC5LzNe

.NET key

Use this when making requests from  
Windows, Xamarin, or Unity clients.

pVGCRB7bKJ2Q3p9VCuywDYwHGw2YzRLk0rympl4V

REST API key

Use this when making requests from server-side REST applications. Keep it secret!

REST key

Y5zbaMrDzYZj0kfD2OchD0qMXZ1gsKNkGqmbJRpP

Webhook key

Use this when implementing a Cloud Code Webhook. Keep it secret!

Webhook key

a3eYeEUQE4W7UjAycj8HGb5OvVEfF5F2Z1sc60nG

File key

Use this key when migrating to your own Parse Server to ensure your new server has access to existing files.

File key

6571cace-b1ca-453b-96f5-82b71e2bc88c

Master key

Using this key overrides all permissions. Not usable on client SDKs. Keep it secret!

Master key

E2YKNY74fhA6W31r6aBoC8M17ONW14nazuME6Vv8
## Código actual funcionando
import React, { useEffect, useState } from 'react';

import { View, Button, Text, SafeAreaView, FlatList, StyleSheet, StatusBar } from 'react-native';

import Parse from 'parse/react-native.js';

import AsyncStorage from '@react-native-async-storage/async-storage';

import axios from 'axios';

  

// Inicializa la conexión a Back4App

const back4appAppId = "T6eE4t3UVT4V3rNe7bONfdcDJIjCozXEY0OXW0b1"; // Reemplaza con tu Application ID

const back4appRestApiKey = "Y5zbaMrDzYZj0kfD2OchD0qMXZ1gsKNkGqmbJRpP"; // Reemplaza con tu REST API key

  

export default function App() {

  const [productos, setProductos] = useState([]);

  

  useEffect(() => {

    fetchProductos();

  }, []);

  

  const fetchProductos = async () => {

    try {

      const response = await axios.get('https://parseapi.back4app.com/parse/classes/Producto', {

        headers: {

          'X-Parse-Application-Id': back4appAppId,

          'X-Parse-REST-API-Key': back4appRestApiKey,

        },

      });

      setProductos(response.data.results.slice(0, 5)); // Selecciona los primeros 3 productos

    } catch (error) {

      console.error('Error al obtener productos:', error);

    }

  };

  

  const renderItem = ({ item }) => (

    <View style={styles.item}>

      <Text style={styles.title}>{item.Producto}</Text>

      <Text style={styles.subtitle}>Precio: {item.Precio}</Text>

    </View>

  );

  

  return (

    <SafeAreaView style={styles.container}>

      <StatusBar backgroundColor="transparent" translucent={true} />

      <FlatList

        data={productos}

        renderItem={renderItem}

        keyExtractor={(item) => item.objectId.toString()}

        style={{ paddingTop: 40 }} // usar

      />  

    </SafeAreaView>

  );

}

  

const styles = StyleSheet.create({

  container: {

    flex: 1,

    backgroundColor: '#fff',

    alignItems: 'center',

    justifyContent: 'center',

  },

  item: {

    padding: 20,

    marginVertical: 8,

    marginHorizontal: 16,

    backgroundColor: '#f9c2ff',

    borderRadius: 10,

  },

  title: {

    fontSize: 24,

    fontWeight: 'bold',

  },

  subtitle: {

    fontSize: 16,

  },

});
## Documentación back4app 
[![Website logo](https://archbee-image-uploads.s3.amazonaws.com/yD3zCY-NNBBIfd0uqcfR5/j4oZZGHTy3LOG033SxIhc_back4app-backend.png)](https://www.back4app.com/)

Ctrl

K

React Native

Parse SDK (REST)

Quickstart

20min

Quickstart[](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk#_Vyb9)

 Introduction[](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk#uE4ih)

In this section you will learn how to get started with Back4App using an existing or new project using the **React Native CLI**. You will install the Parse SDK, initialize Parse using your App keys and make your first API Call saving and reading data objects from Back4App.

 Prerequisites[](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk#jK5s-)

**To complete this tutorial, you will need:**

- An [app created](https://www.back4app.com/docs/get-started/new-parse-app "app created") on Back4App.
    
- ﻿[Npm](https://www.npmjs.com/get-npm?utm_source=house&utm_medium=homepage&utm_campaign=free%20orgs&utm_term=Install%20npm "Npm") or yarn installed.
    
- ﻿[Npx](https://www.npmjs.com/package/npx "Npx") package runner installed.
    

 0 - Create your React Native project[](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk#H82vN)

There are two possible ways to create a project for React Native: Expo and React Native CLI.

**React Native CLI**

**Expo**

 1 - Install dependencies[](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk#T0UlK)

On your React Native project let’s install the Parse Javascript SDK and the Async Storage. Make sure that you have installed npm or yarn in your system.

- **Back4App Parse SDK** - To integrate your App with Back4app servers.
    
- **React Native Async Storage** - To use Parse SDK, an AsyncStorage handler is required.
    

Run the following command on your Project root directory:

npm install parse @react-native-async-storage/async-storage --save

For iOS, use the CocoaPods to add the native RNAsyncStorage to your project:

cd ios & pod install

We are using @react-native-async-storage/async-storage but you can get your favorite AsyncStorage handler.

 2 - Get your App Keys[](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk#Q_wEo)

After creating your App on Back4App, go to your App’s Dashboard and get your App Keys under App Settings->Security & Keys(check the image below). Note that you will always need two keys to connect with Back4App, the Application ID and Javascript KEY.

![Document image](https://images.archbee.com/yD3zCY-NNBBIfd0uqcfR5/AXcOrimmToQQAqPnKxVRD_image.png "Document image")

 3 - Initialize Parse and connect to Back4App[](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk#tFQB8)

Go to your App.js and initialize the Parse SDK using both the Application ID and the Javascript KEY (check the previous step).

App.js

1 // In a React Native application 2 import Parse from "parse/react-native.js"; 3 import AsyncStorage from '@react-native-async-storage/async-storage'; 4 5 6 //Initializing the SDK. 7 Parse.setAsyncStorage(AsyncStorage); 8 //You need to copy BOTH the the Application ID and the Javascript Key from: Dashboard->App Settings->Security & Keys 9 Parse.initialize('YOUR_APPLICATION_ID_HERE','YOUR_JAVASCRIPT_KEY_HERE'); 10 Parse.serverURL = 'https://parseapi.back4app.com/';  

 4 - Save and Read a simple Data Object[](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk#1mw0k)

Your App is initialized and can securely connect to Back4app cloud services. Let’s create two simple functions inside the App.js to save and retrieve data to your Back4App Database.

JS

1 //This funciton will save a simple Person object 2 async function addPerson() { 3 try { 4 //create a new Parse Object instance 5 const newPerson = new Parse.Object('Person'); 6 //define the attributes you want for your Object 7 newPerson.set('name', 'John'); 8 newPerson.set('email', 'john@back4app.com'); 9 //save it on Back4App Data Store 10 await newPerson.save(); 11 } catch (error) { 12 console.log('Error saving new person: ', error); 13 } 14 }  

The above addNewPerson method creates a new Parse.Object representing a person class, sets its properties, then saves it on Back4app cloud data store. Next, implement fetchPerson to fetch the person object you saved on Back4app.

JS

1 const [person, setPerson] = useState(new Parse.Object('Person')); 2 //This function will retrieve a Person which the name is John 3 async function fetchPerson() { 4 //create your Parse Query using the Person Class you've created 5 let query = new Parse.Query('Person'); 6 //run the query to retrieve all objects on Person class, optionally you can add your filters 7 let queryResult = await query.findAll(); 8 //pick the first result 9 const currentPerson = queryResult[0]; 10 //access the Parse Object attributes 11 console.log('person id: ', currentPerson.get('id')); 12 console.log('person name: ', currentPerson.get('name')); 13 console.log('person email: ', currentPerson.get('email')); 14 setPerson(currentPerson); 15 }  

The above method will query a Parse.Object which has the attribute name equals to John. When the query resolves, you will be able to access the person attibutes using the get method.

At this point, your App.js file should look like this:

App.js

1 import React, { useEffect, useState } from 'react'; 2 import { View, Button, Text, SafeAreaView } from 'react-native'; 3 4 // In a React Native application 5 import Parse from 'parse/react-native.js'; 6 import AsyncStorage from '@react-native-async-storage/async-storage'; 7 8 9 //Initializing the SDK 10 Parse.setAsyncStorage(AsyncStorage); 11 //Paste below the Back4App Application ID AND the JavaScript KEY 12 Parse.initialize('YOUR_APPLICATION_ID_HERE', 'YOUR_JAVASCRIPT_KEY_HERE'); 13 //Point to Back4App Parse API address 14 Parse.serverURL = 'https://parseapi.back4app.com/'; 15 16 const App = () => { 17 const [person, setPerson] = useState(new Parse.Object('Person')); 18 19 async function addPerson() { 20 try { 21 //create a new Parse Object instance 22 const newPerson = new Parse.Object('Person'); 23 //define the attributes you want for your Object 24 newPerson.set('name', 'John'); 25 newPerson.set('email', 'john@back4app.com'); 26 //save it on Back4App Data Store 27 await newPerson.save(); 28 } catch (error) { 29 console.log('Error saving new person: ', error); 30 } 31 } 32 33 async function fetchPerson() { 34 //create your Parse Query using the Person Class you've created 35 let query = new Parse.Query('Person'); 36 //run the query to retrieve all objects on Person class, optionally you can add your filters 37 let queryResult = await query.find(); 38 //the resul is an arry of objects. Pick the first result 39 const currentPerson = queryResult[0]; 40 //access the Parse Object attributes 41 console.log('person id: ', currentPerson.get('id')); 42 console.log('person name: ', currentPerson.get('name')); 43 console.log('person email: ', currentPerson.get('email')); 44 setPerson(currentPerson); 45 } 46 47 useEffect(() => { 48 fetchPerson() 49 }, []); 50 51 return ( 52 <SafeAreaView> 53 <View> 54 <Text>Name: {person.get('name')}</Text> 55 <Text>email: {person.get('email')}</Text> 56 <Button title='Add person' onPress={addPerson} /> 57 <Button title='Fetch person' onPress={fetchPerson} /> 58 {/* Your other components here ....*/} 59 </View> 60 </SafeAreaView> 61 ) 62 63 } 64 65 export default App;  

 5 - Test your App[](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk#k7tYi)

1. Open your project’s terminal.
    
2. Run the project.
    

**React Native CLI**

**Expo**

![Document image](https://images.archbee.com/yD3zCY-NNBBIfd0uqcfR5/mEONP4iMWBduxWvn1UkDg_image.png "Document image")

- In case you don’t have a device or a simulator to test it, you can also run it on a web page.
    
- Run npm start and press w.
    

 TroubleShooting[](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk#bZbes)

Some common error messages when running your project:

**Metro has encountered an error: while trying to resolve module “idb-keyval’ from file**

Solution: Go to the metro.conf.js file and change it to this one:

JS

1 const { getDefaultConfig } = require("@expo/metro-config"); 2 const defaultConfig = getDefaultConfig(__dirname); 3 defaultConfig.resolver.assetExts.push("cjs"); 4 module.exports = defaultConfig;  

 **Unable to resolve module ‘EventEmitter’**[](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk#tOcIe)

Solution: Go to the file: node_modules\parse\lib\react-native\EventEmitter.js and change this row:

var EventEmitter = require('../../../react-native/Libraries/vendor/emitter/EventEmitter');

to this:

import EventEmitter from 'react-native/Libraries/vendor/emitter/EventEmitter';

In the same file EventEmitter.js, change the following row:

module.exports = EventEmitter;

to this:

export default EventEmitter;

 What to do next[](https://www.back4app.com/docs/react-native/parse-sdk/react-native-sdk#BrehH)

As you have seen, the easiest way to integrate Back4App into your React Native project is through the [Parse Javascript SDK](https://www.npmjs.com/package/parse "Parse Javascript SDK"). The Parse SDK delivers an excellent development experience through a lightweight and easy-to-use layer that provides minimal configuration, code re-usability, and native optimizations for Android and iOS.

You will find on the following guides how to use features like data storage(relational), real-time capabilities(using a React Hook), local data storage, cloud functions(fully integrated with your database), authentication, file storage, and more. As a next step, we recommend you explore the data storage capabilities and start enjoying the power of Parse Queries.

﻿

Updated 28 Mar 2024

Did this page help you?

Yes

No

[

PREVIOUS

Logging out



](https://www.back4app.com/docs/parse-graphql/graphql-logout-mutation "Logging out")[

NEXT

Start from template

](https://www.back4app.com/docs/react-native/parse-sdk/react-native-template "Start from template")

[Docs powered by Archbee](https://www.archbee.com/?utm_campaign=hosted-docs&utm_medium=referral&utm_source=docs-containers.back4app.com)

https://app.archbee.com/docs/uvBNibJnOtjQHZxUwyV4o/6P2Ujs4m1McHbbOSkf4Up


## Documentacion expo-asset
 Expo Asset

A universal library that allows downloading assets and using them with other libraries.

[

GitHub



](https://github.com/expo/expo/tree/sdk-51/packages/expo-asset "View source code of expo-asset on GitHub")[

npm



](https://www.npmjs.com/package/expo-asset "View package in npm Registry")

Android

iOS

tvOS

Web

---

`expo-asset` provides an interface to Expo's asset system. An asset is any file that lives alongside the source code of your app that the app needs at runtime. Examples include images, fonts, and sounds. Expo's asset system integrates with React Native's, so that you can refer to files with `require('path/to/file')`. This is how you refer to static image files in React Native for use in an `Image` component, for example. Check out React Native's [documentation on static image resources](https://reactnative.dev/docs/images#static-image-resources) for more information. This method of referring to static image resources works out of the box with Expo.

 [Installation](https://docs.expo.dev/versions/latest/sdk/asset/#installation)

Terminal

Copy

`-` `npx expo install expo-asset`

If you're installing this in a [bare React Native app](https://docs.expo.dev/bare/overview/), you should also follow [these additional installation instructions](https://github.com/expo/expo/tree/sdk-51/packages/expo-asset).
 [Configuration in app.json/app.config.js](https://docs.expo.dev/versions/latest/sdk/asset/#configuration-in-appjsonappconfigjs)

You can configure `expo-asset` using its built-in [config plugin](https://docs.expo.dev/config-plugins/introduction/) if you use config plugins in your project ([EAS Build](https://docs.expo.dev/build/introduction/) or `npx expo run:[android|ios]`). The plugin allows you to configure various properties that cannot be set at runtime and require building a new app binary to take effect.
 [Example app.json with config plugin](https://docs.expo.dev/versions/latest/sdk/asset/#example-appjson-with-config-plugin)

app.json

Copy

```
{
  "expo": {
    "plugins": [
      [
        "expo-asset",
        {
          "assets": ["path/to/file.png", "path/to/directory"]
        }
      ]
    ]
  }
}
```

 [Configurable properties](https://docs.expo.dev/versions/latest/sdk/asset/#configurable-properties)

| Name     | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `assets` | `[]`    | An array of asset files or directories to link to the native project. The paths should be relative to the project root so that the file names, whether specified directly or using a directory, will become the resource names.<br><br>Supported file types:<br><br>- Images: `.png`, `.jpg`, `.gif`<br>- Media: `.mp4`, `.mp3`, `.lottie`<br>- SQLite database files: `.db`<br><br>> **Note**: To import an existing database file (`.db`), see instructions in [SQLite API reference](https://docs.expo.dev/versions/latest/sdk/sqlite/#import-an-existing-database). For other file types such as `.lottie`, see [how to add a file extension to `assetExts` in metro config](https://docs.expo.dev/guides/customizing-metro/#adding-more-file-extensions-to-assetexts). |
 [Usage](https://docs.expo.dev/versions/latest/sdk/asset/#usage)

Learn more about how to use the `expo-asset` config plugin to embed an asset file in your project in [Load an asset at build time](https://docs.expo.dev/develop/user-interface/assets/#load-an-asset-at-build-time).
 [API](https://docs.expo.dev/versions/latest/sdk/asset/#api)

```
import { Asset } from 'expo-asset';
```

 [Hooks](https://docs.expo.dev/versions/latest/sdk/asset/#hooks)

 [`useAssets(moduleIds)`](https://docs.expo.dev/versions/latest/sdk/asset/#useassetsmoduleids)

| Name          | Type                 |
| ------------- | -------------------- |
| **moduleIds** | `number \| number[]` |

  

Downloads and stores one or more assets locally. After the assets are loaded, this hook returns a list of asset instances. If something went wrong when loading the assets, an error is returned.

> Note, the assets are not "reloaded" when you dynamically change the asset list.

Returns:

`[[Asset[]](https://docs.expo.dev/versions/latest/sdk/asset/#asset) | undefined, [Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error) | undefined]`

Returns an array containing:

- on the first position, a list of all loaded assets. If they aren't loaded yet, this value is `undefined`.
- on the second position, an error which encountered when loading the assets. If there was no error, this value is `undefined`.

Example

```
const [assets, error] = useAssets([require('path/to/asset.jpg'), require('path/to/other.png')]);

return assets ? <Image source={assets[0]} /> : null;
```

 [Classes](https://docs.expo.dev/versions/latest/sdk/asset/#classes)

 [`Asset`](https://docs.expo.dev/versions/latest/sdk/asset/#asset)

The `Asset` class represents an asset in your app. It gives metadata about the asset (such as its name and type) and provides facilities to load the asset data.

[Asset Properties](https://docs.expo.dev/versions/latest/sdk/asset/#asset-properties)

 [`downloaded`](https://docs.expo.dev/versions/latest/sdk/asset/#downloaded)

Type: `boolean` • Default: `false`

Whether the asset has finished downloading from a call to [`downloadAsync()`](https://docs.expo.dev/versions/latest/sdk/asset/#downloadasync).

 [`hash`](https://docs.expo.dev/versions/latest/sdk/asset/#hash)

Type: `null | string` • Default: `null`

The MD5 hash of the asset's data.
 [`height`](https://docs.expo.dev/versions/latest/sdk/asset/#height)

Type: `null | number` • Default: `null`

If the asset is an image, the height of the image data divided by the scale factor. The scale factor is the number after `@` in the filename, or `1` if not present.

 [`localUri`](https://docs.expo.dev/versions/latest/sdk/asset/#localuri)

Type: `null | string` • Default: `null`

If the asset has been downloaded (by calling [`downloadAsync()`](https://docs.expo.dev/versions/latest/sdk/asset/#downloadasync)), the `file://` URI pointing to the local file on the device that contains the asset data.

 [`name`](https://docs.expo.dev/versions/latest/sdk/asset/#name)

Type: `string`

The name of the asset file without the extension. Also without the part from `@` onward in the filename (used to specify scale factor for images).

 [`type`](https://docs.expo.dev/versions/latest/sdk/asset/#type)

Type: `string`

The extension of the asset filename.
 [`uri`](https://docs.expo.dev/versions/latest/sdk/asset/#uri)

Type: `string`

A URI that points to the asset's data on the remote server. When running the published version of your app, this refers to the location on Expo's asset server where Expo has stored your asset. When running the app from Expo CLI during development, this URI points to Expo CLI's server running on your computer and the asset is served directly from your computer. If you are not using Classic Updates (legacy), this field should be ignored as we ensure your assets are on device before before running your application logic.

 [`width`](https://docs.expo.dev/versions/latest/sdk/asset/#width)

Type: `null | number` • Default: `null`

If the asset is an image, the width of the image data divided by the scale factor. The scale factor is the number after `@` in the filename, or `1` if not present.

[Asset Methods](https://docs.expo.dev/versions/latest/sdk/asset/#asset-methods)

 [`downloadAsync()`](https://docs.expo.dev/versions/latest/sdk/asset/#downloadasync)

Downloads the asset data to a local file in the device's cache directory. Once the returned promise is fulfilled without error, the [`localUri`](https://docs.expo.dev/versions/latest/sdk/asset/#localuri) field of this asset points to a local file containing the asset data. The asset is only downloaded if an up-to-date local file for the asset isn't already present due to an earlier download. The downloaded `Asset` will be returned when the promise is resolved.

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[Asset](https://docs.expo.dev/versions/latest/sdk/asset/#asset)>`

Returns a Promise which fulfills with an `Asset` instance.

 [`fromMetadata(meta)`](https://docs.expo.dev/versions/latest/sdk/asset/#frommetadatameta)

| Name     | Type                                                                              |
| -------- | --------------------------------------------------------------------------------- |
| **meta** | `[AssetMetadata](https://docs.expo.dev/versions/latest/sdk/asset/#assetmetadata)` |

  

Returns:

`[Asset](https://docs.expo.dev/versions/latest/sdk/asset/#asset)`

 [`fromModule(virtualAssetModule)`](https://docs.expo.dev/versions/latest/sdk/asset/#frommodulevirtualassetmodule)

| Name                   | Type               | Description                                                                  |
| ---------------------- | ------------------ | ---------------------------------------------------------------------------- |
| **virtualAssetModule** | `string \| number` | The value of `require('path/to/file')` for the asset or external network URL |

  

Returns the [`Asset`](https://docs.expo.dev/versions/latest/sdk/asset/#asset) instance representing an asset given its module or URL.

Returns:

`[Asset](https://docs.expo.dev/versions/latest/sdk/asset/#asset)`

The [`Asset`](https://docs.expo.dev/versions/latest/sdk/asset/#asset) instance for the asset.

[`fromURI(uri)`](https://docs.expo.dev/versions/latest/sdk/asset/#fromuriuri)

| Name    | Type     |
| ------- | -------- |
| **uri** | `string` |

  

Returns:

`[Asset](https://docs.expo.dev/versions/latest/sdk/asset/#asset)`

 [`loadAsync(moduleId)`](https://docs.expo.dev/versions/latest/sdk/asset/#loadasyncmoduleid)

| Name         | Type                                       | Description                                                                                                          |
| ------------ | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| **moduleId** | `string \| number \| number[] \| string[]` | An array of `require('path/to/file')` or external network URLs. Can also be just one module or URL without an Array. |

  

A helper that wraps `Asset.fromModule(module).downloadAsync` for convenience.

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[Asset[]](https://docs.expo.dev/versions/latest/sdk/asset/#asset)>`

Returns a Promise that fulfills with an array of `Asset`s when the asset(s) has been saved to disk.

Example

```
const [{ localUri }] = await Asset.loadAsync(require('./assets/snack-icon.png'));
```

 [Types](https://docs.expo.dev/versions/latest/sdk/asset/#types)
 [`AssetDescriptor`](https://docs.expo.dev/versions/latest/sdk/asset/#assetdescriptor)

| Name                       | Type             | Description |
| -------------------------- | ---------------- | ----------- |
| **hash**  <br>(optional)   | `string \| null` | -           |
| **height**  <br>(optional) | `number \| null` | -           |
| **name**                   | `string`         | -           |
| **type**                   | `string`         | -           |
| **uri**                    | `string`         | -           |
| **width**  <br>(optional)  | `number \| null` | -           |

 [`AssetMetadata`](https://docs.expo.dev/versions/latest/sdk/asset/#assetmetadata)

Type: `[Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[PackagerAsset](https://github.com/facebook/react-native/blob/main/packages/assets/registry.js), 'httpServerLocation' | 'name' | 'hash' | 'type' | 'scales' | 'width' | 'height'>` extended by:

  

| Name                           | Type       | Description |
| ------------------------------ | ---------- | ----------- |
| **fileHashes**  <br>(optional) | `string[]` | -           |
| **fileUris**  <br>(optional)   | `string[]` | -           |
| **uri**  <br>(optional)        | `string`   | -           |
## Documentación expo-sqlite
Expo SQLite

A library that provides access to a database that can be queried through a SQLite API.

[

GitHub



](https://github.com/expo/expo/tree/sdk-51/packages/expo-sqlite "View source code of expo-sqlite on GitHub")[

npm



](https://www.npmjs.com/package/expo-sqlite "View package in npm Registry")

Android

iOS

---

`expo-sqlite` gives your app access to a database that can be queried through a SQLite API. The database is persisted across restarts of your app.

 [Installation](https://docs.expo.dev/versions/latest/sdk/sqlite/#installation)

Terminal

Copy

`-` `npx expo install expo-sqlite`

If you're installing this in a [bare React Native app](https://docs.expo.dev/bare/overview/), you should also follow [these additional installation instructions](https://github.com/expo/expo/tree/sdk-51/packages/expo-sqlite).

 [Usage](https://docs.expo.dev/versions/latest/sdk/sqlite/#usage)

Import the module from `expo-sqlite`.

Import the module from expo-sqlite

Copy

```
import * as SQLite from 'expo-sqlite';
```

 [Basic CRUD operations](https://docs.expo.dev/versions/latest/sdk/sqlite/#basic-crud-operations)

Basic CRUD operations

Copy

```
const db = await SQLite.openDatabaseAsync('databaseName');

// `execAsync()` is useful for bulk queries when you want to execute altogether.
// Please note that `execAsync()` does not escape parameters and may lead to SQL injection.
await db.execAsync(`
PRAGMA journal_mode = WAL;
CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY NOT NULL, value TEXT NOT NULL, intValue INTEGER);
INSERT INTO test (value, intValue) VALUES ('test1', 123);
INSERT INTO test (value, intValue) VALUES ('test2', 456);
INSERT INTO test (value, intValue) VALUES ('test3', 789);
`);

// `runAsync()` is useful when you want to execute some write operations.
const result = await db.runAsync('INSERT INTO test (value, intValue) VALUES (?, ?)', 'aaa', 100);
console.log(result.lastInsertRowId, result.changes);
await db.runAsync('UPDATE test SET intValue = ? WHERE value = ?', 999, 'aaa'); // Binding unnamed parameters from variadic arguments
await db.runAsync('UPDATE test SET intValue = ? WHERE value = ?', [999, 'aaa']); // Binding unnamed parameters from array
await db.runAsync('DELETE FROM test WHERE value = $value', { $value: 'aaa' }); // Binding named parameters from object

// `getFirstAsync()` is useful when you want to get a single row from the database.
const firstRow = await db.getFirstAsync('SELECT * FROM test');
console.log(firstRow.id, firstRow.value, firstRow.intValue);

// `getAllAsync()` is useful when you want to get all results as an array of objects.
const allRows = await db.getAllAsync('SELECT * FROM test');
for (const row of allRows) {
  console.log(row.id, row.value, row.intValue);
}

// `getEachAsync()` is useful when you want to iterate SQLite query cursor.
for await (const row of db.getEachAsync('SELECT * FROM test')) {
  console.log(row.id, row.value, row.intValue);
}
```

 [Prepared statements](https://docs.expo.dev/versions/latest/sdk/sqlite/#prepared-statements)

Prepared statement allows you compile your SQL query once and execute it multiple times with different parameters. You can get a prepared statement by calling [`prepareAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#prepareasyncsource) or [`prepareSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#preparesyncsource) method on a database instance. The prepared statement can fulfill CRUD operations by calling [`executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executeasyncparams) or [`executeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executesyncparams) method.

> **Note:** Remember to call [`finalizeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizeasync) or [`finalizeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizesync) method to release the prepared statement after you finish using the statement. `try-finally` block is recommended to ensure the prepared statement is finalized.

Prepared statements

Copy

```
const statement = await db.prepareAsync(
  'INSERT INTO test (value, intValue) VALUES ($value, $intValue)'
);
try {
  let result = await statement.executeAsync({ $value: 'bbb', $intValue: 101 });
  console.log('bbb and 101:', result.lastInsertRowId, result.changes);

  result = await statement.executeAsync({ $value: 'ccc', $intValue: 102 });
  console.log('ccc and 102:', result.lastInsertRowId, result.changes);

  result = await statement.executeAsync({ $value: 'ddd', $intValue: 103 });
  console.log('ddd and 103:', result.lastInsertRowId, result.changes);
} finally {
  await statement.finalizeAsync();
}

const statement2 = await db.prepareAsync('SELECT * FROM test WHERE intValue >= $intValue');
try {
  const result = await statement2.executeAsync<{ value: string; intValue: number }>({
    $intValue: 100,
  });

  // `getFirstAsync()` is useful when you want to get a single row from the database.
  const firstRow = await result.getFirstAsync();
  console.log(firstRow.id, firstRow.value, firstRow.intValue);

  // Reset the SQLite query cursor to the beginning for the next `getAllAsync()` call.
  await result.resetAsync();

  // `getAllAsync()` is useful when you want to get all results as an array of objects.
  const allRows = await result.getAllAsync();
  for (const row of allRows) {
    console.log(row.value, row.intValue);
  }

  // Reset the SQLite query cursor to the beginning for the next `for-await-of` loop.
  await result.resetAsync();

  // The result object is also an async iterable. You can use it in `for-await-of` loop to iterate SQLite query cursor.
  for await (const row of result) {
    console.log(row.value, row.intValue);
  }
} finally {
  await statement2.finalizeAsync();
}
```

 [`useSQLiteContext()` hook](https://docs.expo.dev/versions/latest/sdk/sqlite/#usesqlitecontext-hook)

useSQLiteContext() hook

Copy

```
import { SQLiteProvider, useSQLiteContext, type SQLiteDatabase } from 'expo-sqlite';
import { useEffect, useState } from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <SQLiteProvider databaseName="test.db" onInit={migrateDbIfNeeded}>
        <Header />
        <Content />
      </SQLiteProvider>
    </View>
  );
}

export function Header() {
  const db = useSQLiteContext();
  const [version, setVersion] = useState('');
  useEffect(() => {
    async function setup() {
      const result = await db.getFirstAsync<{ 'sqlite_version()': string }>(
        'SELECT sqlite_version()'
      );
      setVersion(result['sqlite_version()']);
    }
    setup();
  }, []);
  return (
    <View style={styles.headerContainer}>
      <Text style={styles.headerText}>SQLite version: {version}</Text>
    </View>
  );
}

interface Todo {
  value: string;
  intValue: number;
}

export function Content() {
  const db = useSQLiteContext();
  const [todos, setTodos] = useState<Todo[]>([]);

  useEffect(() => {
    async function setup() {
      const result = await db.getAllAsync<Todo>('SELECT * FROM todos');
      setTodos(result);
    }
    setup();
  }, []);

  return (
    <View style={styles.contentContainer}>
      {todos.map((todo, index) => (
        <View style={styles.todoItemContainer} key={index}>
          <Text>{`${todo.intValue} - ${todo.value}`}</Text>
        </View>
      ))}
    </View>
  );
}

async function migrateDbIfNeeded(db: SQLiteDatabase) {
  const DATABASE_VERSION = 1;
  let { user_version: currentDbVersion } = await db.getFirstAsync<{ user_version: number }>(
    'PRAGMA user_version'
  );
  if (currentDbVersion >= DATABASE_VERSION) {
    return;
  }
  if (currentDbVersion === 0) {
    await db.execAsync(`
PRAGMA journal_mode = 'wal';
CREATE TABLE todos (id INTEGER PRIMARY KEY NOT NULL, value TEXT NOT NULL, intValue INTEGER);
`);
    await db.runAsync('INSERT INTO todos (value, intValue) VALUES (?, ?)', 'hello', 1);
    await db.runAsync('INSERT INTO todos (value, intValue) VALUES (?, ?)', 'world', 2);
    currentDbVersion = 1;
  }
  // if (currentDbVersion === 1) {
  //   Add more migrations
  // }
  await db.execAsync(`PRAGMA user_version = ${DATABASE_VERSION}`);
}

const styles = StyleSheet.create({
  // Your styles...
});
```

 [`useSQLiteContext()` hook with `React.Suspense`](https://docs.expo.dev/versions/latest/sdk/sqlite/#usesqlitecontext-hook-with-reactsuspense)

As with the [`useSQLiteContext()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#usesqlitecontext-hook) hook, you can also integrate the [`SQLiteProvider`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteprovider) with [`React.Suspense`](https://react.dev/reference/react/Suspense) to show a fallback component until the database is ready. To enable the integration, pass the `useSuspense` prop to the `SQLiteProvider` component.

useSQLiteContext() hook with React.Suspense

Copy

```
import { SQLiteProvider, useSQLiteContext } from 'expo-sqlite';
import { Suspense } from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <Suspense fallback={<Fallback />}>
        <SQLiteProvider databaseName="test.db" onInit={migrateDbIfNeeded} useSuspense>
          <Header />
          <Content />
        </SQLiteProvider>
      </Suspense>
    </View>
  );
}
```

 [Executing queries within an async transaction](https://docs.expo.dev/versions/latest/sdk/sqlite/#executing-queries-within-an-async-transaction)

Executing queries within an async transaction

Copy

```
const db = await SQLite.openDatabaseAsync('databaseName');

await db.withTransactionAsync(async () => {
  const result = await db.getFirstAsync('SELECT COUNT(*) FROM USERS');
  console.log('Count:', result.rows[0]['COUNT(*)']);
});
```

Due to the nature of async/await, any query that runs while the transaction is active will be included in the transaction. This includes query statements that are outside of the scope function passed to `withTransactionAsync()` and may be surprising behavior. For example, the following test case runs queries inside and outside of a scope function passed to `withTransactionAsync()`. However, all of the queries will run within the actual SQL transaction because the second `UPDATE` query runs before the transaction finishes.

```
Promise.all([
  // 1. A new transaction begins
  db.withTransactionAsync(async () => {
    // 2. The value "first" is inserted into the test table and we wait 2
    //    seconds
    await db.execAsync('INSERT INTO test (data) VALUES ("first")');
    await sleep(2000);

    // 4. Two seconds in, we read the latest data from the table
    const row = await db.getFirstAsync<{ data: string }>('SELECT data FROM test');

    // ❌ The data in the table will be "second" and this expectation will fail.
    //    Additionally, this expectation will throw an error and roll back the
    //    transaction, including the `UPDATE` query below since it ran within
    //    the transaction.
    expect(row.data).toBe('first');
  }),
  // 3. One second in, the data in the test table is updated to be "second".
  //    This `UPDATE` query runs in the transaction even though its code is
  //    outside of it because the transaction happens to be active at the time
  //    this query runs.
  sleep(1000).then(async () => db.execAsync('UPDATE test SET data = "second"')),
]);
```

The [`withExclusiveTransactionAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#withexclusivetransactionasynctask) function addresses this. Only queries that run within the scope function passed to `withExclusiveTransactionAsync()` will run within the actual SQL transaction.

 [Executing PRAGMA queries](https://docs.expo.dev/versions/latest/sdk/sqlite/#executing-pragma-queries)

Executing PRAGMA queries

Copy

```
const db = await SQLite.openDatabaseAsync('databaseName');
await db.execAsync('PRAGMA journal_mode = WAL');
await db.execAsync('PRAGMA foreign_keys = ON');
```

> **Tip:** Enable [WAL journal mode](https://www.sqlite.org/wal.html) when you create a new database to improve performance in general.

 [Import an existing database](https://docs.expo.dev/versions/latest/sdk/sqlite/#import-an-existing-database)

To open a new SQLite database using an existing **.db** file you already have, you can use the [`SQLiteProvider`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteprovider) with [`assetSource`](https://docs.expo.dev/versions/latest/sdk/sqlite/#assetsource).

useSQLiteContext() with existing database

Copy

```
import { SQLiteProvider, useSQLiteContext } from 'expo-sqlite';
import { View, Text, StyleSheet } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
      <SQLiteProvider databaseName="test.db" assetSource={{ assetId: require('./assets/test.db') }}>
        <Header />
        <Content />
      </SQLiteProvider>
    </View>
  );
}
```

 [Passing binary data](https://docs.expo.dev/versions/latest/sdk/sqlite/#passing-binary-data)

Use [`Uint8Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array) to pass binary data to the database:

Passing binary data

Copy

```
await db.execAsync(`
DROP TABLE IF EXISTS blobs;
CREATE TABLE IF NOT EXISTS blobs (id INTEGER PRIMARY KEY NOT NULL, data BLOB);
`);

const blob = new Uint8Array([0x00, 0x01, 0x02, 0x03, 0x04, 0x05]);
await db.runAsync('INSERT INTO blobs (data) VALUES (?)', blob);

const row = await db.getFirstAsync<{ data: Uint8Array }>('SELECT * FROM blobs');
expect(row.data).toEqual(blob);
```

 [Third-party library integrations](https://docs.expo.dev/versions/latest/sdk/sqlite/#third-party-library-integrations)

The `expo-sqlite` library is designed to be a solid SQLite foundation. It enables broader integrations with third-party libraries for more advanced higher-level features. Here are some of the libraries that you can use with `expo-sqlite`.

 [Drizzle ORM](https://docs.expo.dev/versions/latest/sdk/sqlite/#drizzle-orm)

[Drizzle](https://orm.drizzle.team/) is a ["headless TypeScript ORM with a head"](https://orm.drizzle.team/docs/overview). It runs on Node.js, Bun, Deno, and React Native. It also has a CLI compansion called [`drizzle-kit`](https://orm.drizzle.team/kit-docs/overview) for generating SQL migrations.

Check out the [Drizzle ORM documentation](https://orm.drizzle.team/) and the [`expo-sqlite` integration guide](https://orm.drizzle.team/docs/get-started-sqlite#expo-sqlite) for more details.

 [Knex.js](https://docs.expo.dev/versions/latest/sdk/sqlite/#knexjs)

[Knex.js](https://knexjs.org/) is a SQL query builder that is ["flexible, portable, and fun to use!"](https://github.com/knex/knex)

Check out the [`expo-sqlite` integration guide](https://github.com/expo/knex-expo-sqlite-dialect) for more details.

 [API](https://docs.expo.dev/versions/latest/sdk/sqlite/#api)
 [Cheatsheet for the common API](https://docs.expo.dev/versions/latest/sdk/sqlite/#cheatsheet-for-the-common-api)
The following table summarizes the common API for [`SQLiteDatabase`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedatabase) and [`SQLiteStatement`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitestatement) classes:

|[`SQLiteDatabase`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedatabase) methods|[`SQLiteStatement`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitestatement) methods|Description|Use Case|
|---|---|---|---|
|[`runAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#runasyncsource-params)|[`executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executeasyncparams)|Executes a SQL query, returning information on the changes made.|Ideal for SQL write operations such as `INSERT`, `UPDATE`, `DELETE`.|
|[`getFirstAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getfirstasyncsource-params)|[`executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executeasyncparams) + [`getFirstAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getfirstasync)|Retrieves the first row from the query result.|Suitable for fetching a single row from the database. For example: `getFirstAsync('SELECT * FROM Users WHERE id = ?', userId)`.|
|[`getAllAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getallasyncsource-params)|[`executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executeasyncparams) + [`getFirstAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getallasync)|Fetches all query results at once.|Best suited for scenarios with smaller result sets, such as queries with a LIMIT clause, like `SELECT * FROM Table LIMIT 100`, where you intend to retrieve all results in a single batch.|
|[`getEachAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#geteachasyncsource-params)|[`executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executeasyncparams) + `for-await-of` async iterator|Provides an iterator for result set traversal. This method fetches one row at a time from the database, potentially reducing memory usage compared to `getAllAsync()`.|Recommended for handling large result sets incrementally, such as with infinite scrolling implementations.|

 [Component](https://docs.expo.dev/versions/latest/sdk/sqlite/#component)

 [`SQLiteProvider`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteprovider)

Type: `React.Element<[SQLiteProviderProps](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteproviderprops)>`

Context.Provider component that provides a SQLite database to all children. All descendants of this component will be able to access the database using the [`useSQLiteContext`](https://docs.expo.dev/versions/latest/sdk/sqlite/#usesqlitecontext) hook.

[SQLiteProviderProps](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteproviderprops)

 [`assetSource`](https://docs.expo.dev/versions/latest/sdk/sqlite/#assetsource)

Optional • Type: `[SQLiteProviderAssetSource](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteproviderassetsource)`

Import a bundled database file from the specified asset module.

Example

```
assetSource={{ assetId: require('./assets/db.db') }}
```

 [`children`](https://docs.expo.dev/versions/latest/sdk/sqlite/#children)

Type: `[ReactNode](https://reactnative.dev/docs/react-node)`

The children to render.

 [`databaseName`](https://docs.expo.dev/versions/latest/sdk/sqlite/#databasename)

Type: `string`

The name of the database file to open.

 [`onError`](https://docs.expo.dev/versions/latest/sdk/sqlite/#onerror)

Optional • Type: `(error: [Error](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)) => void` • Default: `rethrow the error`

Handle errors from SQLiteProvider.

 [`onInit`](https://docs.expo.dev/versions/latest/sdk/sqlite/#oninit)

Optional • Type: `(db: [SQLiteDatabase](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedatabase)) => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`

A custom initialization handler to run before rendering the children. You can use this to run database migrations or other setup tasks.

 [`options`](https://docs.expo.dev/versions/latest/sdk/sqlite/#options)

Optional • Type: `[SQLiteOpenOptions](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteopenoptions)`

Open options.

 [`useSuspense`](https://docs.expo.dev/versions/latest/sdk/sqlite/#usesuspense)

Optional • Type: `boolean` • Default: `false`

Enable [`React.Suspense`](https://react.dev/reference/react/Suspense) integration.

Example

```
export default function App() {
  return (
    <Suspense fallback={<Text>Loading...</Text>}>
      <SQLiteProvider databaseName="test.db" useSuspense={true}>
        <Main />
      </SQLiteProvider>
    </Suspense>
  );
}
```

 [Hooks](https://docs.expo.dev/versions/latest/sdk/sqlite/#hooks)

 [`useSQLiteContext()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#usesqlitecontext)

A global hook for accessing the SQLite database across components. This hook should only be used within a [`<SQLiteProvider>`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteprovider) component.

Returns:

`[SQLiteDatabase](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedatabase)`

Example

```
export default function App() {
  return (
    <SQLiteProvider databaseName="test.db">
      <Main />
    </SQLiteProvider>
  );
}

export function Main() {
  const db = useSQLiteContext();
  console.log('sqlite version', db.getSync('SELECT sqlite_version()'));
  return <View />
}
```

 [Classes](https://docs.expo.dev/versions/latest/sdk/sqlite/#classes)

 [`SQLiteDatabase`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedatabase)

A SQLite database.

SQLiteDatabase Properties

 [`databaseName`](https://docs.expo.dev/versions/latest/sdk/sqlite/#databasename-1)

Type: `string`

 [`options`](https://docs.expo.dev/versions/latest/sdk/sqlite/#options-1)

Type: `[SQLiteOpenOptions](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteopenoptions)`

SQLiteDatabase Methods

 [`closeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#closeasync)

Close the database.

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`

 [`closeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#closesync)

Close the database.

Returns:

`void`

 [`execAsync(source)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#execasyncsource)

| Name       | Type     | Description                              |
| ---------- | -------- | ---------------------------------------- |
| **source** | `string` | A string containing all the SQL queries. |

  

Execute all SQL queries in the supplied string.

> Note: The queries are not escaped for you! Be careful when constructing your queries.

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`

 [`execSync(source)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#execsyncsource)

|Name|Type|Description|
|---|---|---|
|**source**|`string`|A string containing all the SQL queries.|

  

Execute all SQL queries in the supplied string.

> **Note:** The queries are not escaped for you! Be careful when constructing your queries.

> **Note:** Running heavy tasks with this function can block the JavaScript thread and affect performance.

Returns:

`void`

 [`getAllAsync<T>(source, params)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getallasynctsource-params)

|Name|Type|Description|
|---|---|---|
|**source**|`string`|A string containing the SQL query.|
|**params**|`[SQLiteBindParams](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`|The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.|

  

A convenience wrapper around [`SQLiteDatabase.prepareAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#prepareasyncsource), [`SQLiteStatement.executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executeasyncparams), [`SQLiteExecuteAsyncResult.getAllAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getallasync), and [`SQLiteStatement.finalizeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizeasync).

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<T[]>`

Example

```
// For unnamed parameters, you pass values in an array.
db.getAllAsync('SELECT * FROM test WHERE intValue = ? AND name = ?', [1, 'Hello']);

// For unnamed parameters, you pass values in variadic arguments.
db.getAllAsync('SELECT * FROM test WHERE intValue = ? AND name = ?', 1, 'Hello');

// For named parameters, you should pass values in object.
db.getAllAsync('SELECT * FROM test WHERE intValue = $intValue AND name = $name', { $intValue: 1, $name: 'Hello' });
```

 [`getAllSync<T>(source, params)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getallsynctsource-params)

|Name|Type|Description|
|---|---|---|
|**source**|`string`|A string containing the SQL query.|
|**params**|`[SQLiteBindParams](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`|The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.|

  

A convenience wrapper around [`SQLiteDatabase.prepareSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#preparesyncsource), [`SQLiteStatement.executeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executesyncparams), [`SQLiteExecuteSyncResult.getAllSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getallsync), and [`SQLiteStatement.finalizeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizesync).

> **Note:** Running heavy tasks with this function can block the JavaScript thread and affect performance.

Returns:

`T[]`

 [`getEachAsync<T>(source, params)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#geteachasynctsource-params)

|Name|Type|Description|
|---|---|---|
|**source**|`string`|A string containing the SQL query.|
|**params**|`[SQLiteBindParams](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`|The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.|

  

A convenience wrapper around [`SQLiteDatabase.prepareAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#prepareasyncsource), [`SQLiteStatement.executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executeasyncparams), [`SQLiteExecuteAsyncResult`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteexecuteasyncresult) `AsyncIterator`, and [`SQLiteStatement.finalizeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizeasync).

Returns:

`[AsyncIterableIterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator)<T>`

Rather than returning Promise, this function returns an [`AsyncIterableIterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator). You can use `for await...of` to iterate over the rows from the SQLite query result.

 [`getEachSync<T>(source, params)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#geteachsynctsource-params)

| Name       | Type                                                                                     | Description                                                                                                                                                                                                                                          |
| ---------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **source** | `string`                                                                                 | A string containing the SQL query.                                                                                                                                                                                                                   |
| **params** | `[SQLiteBindParams](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)` | The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values. |

  

A convenience wrapper around [`SQLiteDatabase.prepareSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#preparesyncsource), [`SQLiteStatement.executeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executesyncparams), [`SQLiteExecuteSyncResult`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteexecutesyncresult) `Iterator`, and [`SQLiteStatement.finalizeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizesync).

> **Note:** Running heavy tasks with this function can block the JavaScript thread and affect performance.

Returns:

`[IterableIterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)<T>`

This function returns an [`IterableIterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator). You can use `for...of` to iterate over the rows from the SQLite query result.

 [`getFirstAsync<T>(source, params)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getfirstasynctsource-params)

|Name|Type|Description|
|---|---|---|
|**source**|`string`|A string containing the SQL query.|
|**params**|`[SQLiteBindParams](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`|The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.|

  

A convenience wrapper around [`SQLiteDatabase.prepareAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#prepareasyncsource), [`SQLiteStatement.executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executeasyncparams), [`SQLiteExecuteAsyncResult.getFirstAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getfirstasync), and [`SQLiteStatement.finalizeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizeasync).

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<null | T>`

 [`getFirstSync<T>(source, params)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getfirstsynctsource-params)

|Name|Type|Description|
|---|---|---|
|**source**|`string`|A string containing the SQL query.|
|**params**|`[SQLiteBindParams](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`|The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.|

  

A convenience wrapper around [`SQLiteDatabase.prepareSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#preparesyncsource), [`SQLiteStatement.executeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executesyncparams), [`SQLiteExecuteSyncResult.getFirstSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getfirstsync), and [`SQLiteStatement.finalizeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizesync).

> **Note:** Running heavy tasks with this function can block the JavaScript thread and affect performance.

Returns:

`null | T`

 [`isInTransactionAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#isintransactionasync)

Asynchronous call to return whether the database is currently in a transaction.

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<boolean>`

 [`isInTransactionSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#isintransactionsync)

Synchronous call to return whether the database is currently in a transaction.

Returns:

`boolean`

 [`prepareAsync(source)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#prepareasyncsource)

|Name|Type|Description|
|---|---|---|
|**source**|`string`|A string containing the SQL query.|

  

Create a [prepared SQLite statement](https://www.sqlite.org/c3ref/prepare.html).

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[SQLiteStatement](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitestatement)>`

 [`prepareSync(source)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#preparesyncsource)

|Name|Type|Description|
|---|---|---|
|**source**|`string`|A string containing the SQL query.|

  

Create a [prepared SQLite statement](https://www.sqlite.org/c3ref/prepare.html).

> **Note:** Running heavy tasks with this function can block the JavaScript thread and affect performance.

Returns:

`[SQLiteStatement](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitestatement)`

 [`runAsync(source, params)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#runasyncsource-params)

|Name|Type|Description|
|---|---|---|
|**source**|`string`|A string containing the SQL query.|
|**params**|`[SQLiteBindParams](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`|The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.|

  

A convenience wrapper around [`SQLiteDatabase.prepareAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#prepareasyncsource), [`SQLiteStatement.executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executeasyncparams), and [`SQLiteStatement.finalizeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizeasync).

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[SQLiteRunResult](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliterunresult)>`

 [`runSync(source, params)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#runsyncsource-params)

|Name|Type|Description|
|---|---|---|
|**source**|`string`|A string containing the SQL query.|
|**params**|`[SQLiteBindParams](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`|The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.|

  

A convenience wrapper around [`SQLiteDatabase.prepareSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#preparesyncsource), [`SQLiteStatement.executeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executesyncparams), and [`SQLiteStatement.finalizeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizesync).

> **Note:** Running heavy tasks with this function can block the JavaScript thread and affect performance.

Returns:

`[SQLiteRunResult](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliterunresult)`

 [`serializeAsync(databaseName)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#serializeasyncdatabasename)

|Name|Type|Description|
|---|---|---|
|**databaseName**  <br>(optional)|`string`|The name of the current attached databases. The default value is `main` which is the default database name.<br><br>Default: `'main'`|

  

[Serialize the database](https://sqlite.org/c3ref/serialize.html) as `Uint8Array`.

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<Uint8Array>`

 [`serializeSync(databaseName)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#serializesyncdatabasename)

|Name|Type|Description|
|---|---|---|
|**databaseName**  <br>(optional)|`string`|The name of the current attached databases. The default value is `main` which is the default database name.<br><br>Default: `'main'`|

  

[Serialize the database](https://sqlite.org/c3ref/serialize.html) as `Uint8Array`.

> **Note:** Running heavy tasks with this function can block the JavaScript thread and affect performance.

Returns:

`Uint8Array`

 [`withExclusiveTransactionAsync(task)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#withexclusivetransactionasynctask)

|Name|Type|Description|
|---|---|---|
|**task**|`(txn: [Transaction](https://docs.expo.dev/versions/latest/sdk/sqlite/#transaction)) => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`|An async function to execute within a transaction. Any queries inside the transaction must be executed on the `txn` object. The `txn` object has the same interfaces as the [`SQLiteDatabase`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedatabase) object. You can use `txn` like a [`SQLiteDatabase`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedatabase) object.|

  

Execute a transaction and automatically commit/rollback based on the `task` result.

The transaction may be exclusive. As long as the transaction is converted into a write transaction, the other async write queries will abort with `database is locked` error.

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`

Example

```
db.withExclusiveTransactionAsync(async (txn) => {
  await txn.execAsync('UPDATE test SET name = "aaa"');
});
```

 [`withTransactionAsync(task)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#withtransactionasynctask)

| Name     | Type                                                                                                              | Description                                        |
| -------- | ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **task** | `() => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>` | An async function to execute within a transaction. |

  

Execute a transaction and automatically commit/rollback based on the `task` result.

> **Note:** This transaction is not exclusive and can be interrupted by other async queries.

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`

Example

```
db.withTransactionAsync(async () => {
  await db.execAsync('UPDATE test SET name = "aaa"');

  //
  // We cannot control the order of async/await order, so order of execution is not guaranteed.
  // The following UPDATE query out of transaction may be executed here and break the expectation.
  //

  const result = await db.getAsync<{ name: string }>('SELECT name FROM Users');
  expect(result?.name).toBe('aaa');
});
db.execAsync('UPDATE test SET name = "bbb"');
```

If you worry about the order of execution, use `withExclusiveTransactionAsync` instead.

 [`withTransactionSync(task)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#withtransactionsynctask)

|Name|Type|Description|
|---|---|---|
|**task**|`() => void`|An async function to execute within a transaction.|

  

Execute a transaction and automatically commit/rollback based on the `task` result.

> **Note:** Running heavy tasks with this function can block the JavaScript thread and affect performance.

Returns:

`void`

 [`SQLiteStatement`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitestatement)

A prepared statement returned by [`SQLiteDatabase.prepareAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#prepareasyncsource) or [`SQLiteDatabase.prepareSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#preparesyncsource) that can be binded with parameters and executed.

SQLiteStatement Methods

 [`executeAsync<T>(params)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executeasynctparams)

|Name|Type|Description|
|---|---|---|
|**params**|`[SQLiteBindParams](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`|The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.|

  

Run the prepared statement and return the [`SQLiteExecuteAsyncResult`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteexecuteasyncresult) instance.

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[SQLiteExecuteAsyncResult](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteexecuteasyncresult)<T>>`

 [`executeSync<T>(params)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executesynctparams)

|Name|Type|Description|
|---|---|---|
|**params**|`[SQLiteBindParams](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)`|The parameters to bind to the prepared statement. You can pass values in array, object, or variadic arguments. See [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue) for more information about binding values.|

  

Run the prepared statement and return the [`SQLiteExecuteSyncResult`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteexecutesyncresult) instance.

> **Note:** Running heavy tasks with this function can block the JavaScript thread and affect performance.

Returns:

`[SQLiteExecuteSyncResult](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteexecutesyncresult)<T>`

 [`finalizeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizeasync)

Finalize the prepared statement. This will call the [`sqlite3_finalize()`](https://www.sqlite.org/c3ref/finalize.html) C function under the hood.

Attempting to access a finalized statement will result in an error.

> **Note:** While expo-sqlite will automatically finalize any orphaned prepared statements upon closing the database, it is considered best practice to manually finalize prepared statements as soon as they are no longer needed. This helps to prevent resource leaks. You can use the `try...finally` statement to ensure that prepared statements are finalized even if an error occurs.

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`

 [`finalizeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#finalizesync)

Finalize the prepared statement. This will call the [`sqlite3_finalize()`](https://www.sqlite.org/c3ref/finalize.html) C function under the hood.

Attempting to access a finalized statement will result in an error.

> **Note:** While expo-sqlite will automatically finalize any orphaned prepared statements upon closing the database, it is considered best practice to manually finalize prepared statements as soon as they are no longer needed. This helps to prevent resource leaks. You can use the `try...finally` statement to ensure that prepared statements are finalized even if an error occurs.

Returns:

`void`

 [`getColumnNamesAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getcolumnnamesasync)

Get the column names of the prepared statement.

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<string[]>`

 [`getColumnNamesSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getcolumnnamessync)

Get the column names of the prepared statement.

Returns:

`string[]`

 [Methods](https://docs.expo.dev/versions/latest/sdk/sqlite/#methods)

 [`SQLite.deleteDatabaseAsync(databaseName)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedeletedatabaseasyncdatabasename)

| Name             | Type     | Description                              |
| ---------------- | -------- | ---------------------------------------- |
| **databaseName** | `string` | The name of the database file to delete. |

  

Delete a database file.

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`

 [`SQLite.deleteDatabaseSync(databaseName)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedeletedatabasesyncdatabasename)

|Name|Type|Description|
|---|---|---|
|**databaseName**|`string`|The name of the database file to delete.|

  

Delete a database file.

> **Note:** Running heavy tasks with this function can block the JavaScript thread and affect performance.

Returns:

`void`

 [`SQLite.deserializeDatabaseAsync(serializedData, options)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedeserializedatabaseasyncserializeddata-options)

|Name|Type|Description|
|---|---|---|
|**serializedData**|`Uint8Array`|The binary array to deserialize from [`SQLiteDatabase.serializeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#serializeasyncdatabasename).|
|**options**  <br>(optional)|`[SQLiteOpenOptions](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteopenoptions)`|Open options.|

  

Given a `Uint8Array` data and [deserialize to memory database](https://sqlite.org/c3ref/deserialize.html).

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[SQLiteDatabase](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedatabase)>`

 [`SQLite.deserializeDatabaseSync(serializedData, options)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedeserializedatabasesyncserializeddata-options)

|Name|Type|Description|
|---|---|---|
|**serializedData**|`Uint8Array`|The binary array to deserialize from [`SQLiteDatabase.serializeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#serializesyncdatabasename)|
|**options**  <br>(optional)|`[SQLiteOpenOptions](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteopenoptions)`|Open options.|

  

Given a `Uint8Array` data and [deserialize to memory database](https://sqlite.org/c3ref/deserialize.html).

> **Note:** Running heavy tasks with this function can block the JavaScript thread and affect performance.

Returns:

`[SQLiteDatabase](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedatabase)`

 [`SQLite.openDatabaseAsync(databaseName, options)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteopendatabaseasyncdatabasename-options)

|Name|Type|Description|
|---|---|---|
|**databaseName**|`string`|The name of the database file to open.|
|**options**  <br>(optional)|`[SQLiteOpenOptions](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteopenoptions)`|Open options.|

  

Open a database.

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[SQLiteDatabase](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedatabase)>`

 [`SQLite.openDatabaseSync(databaseName, options)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteopendatabasesyncdatabasename-options)

|Name|Type|Description|
|---|---|---|
|**databaseName**|`string`|The name of the database file to open.|
|**options**  <br>(optional)|`[SQLiteOpenOptions](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteopenoptions)`|Open options.|

  

Open a database.

> **Note:** Running heavy tasks with this function can block the JavaScript thread and affect performance.

Returns:

`[SQLiteDatabase](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitedatabase)`

 [Event Subscriptions](https://docs.expo.dev/versions/latest/sdk/sqlite/#event-subscriptions)

 [`SQLite.addDatabaseChangeListener(listener)`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteadddatabasechangelistenerlistener)

|Name|Type|Description|
|---|---|---|
|**listener**|`(event: [DatabaseChangeEvent](https://docs.expo.dev/versions/latest/sdk/sqlite/#databasechangeevent)) => void`|A function that receives the `databaseName`, `databaseFilePath`, `tableName` and `rowId` of the modified data.|

  

Add a listener for database changes.

> Note: to enable this feature, you must set [`enableChangeListener` to `true`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteopenoptions) when opening the database.

Returns:

`[Subscription](https://docs.expo.dev/versions/latest/sdk/sqlite/#subscription)`

A `Subscription` object that you can call `remove()` on when you would like to unsubscribe the listener.

 [Interfaces](https://docs.expo.dev/versions/latest/sdk/sqlite/#interfaces)

 [`SQLiteExecuteAsyncResult`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteexecuteasyncresult)

Extends: `[AsyncIterableIterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AsyncIterator)<T>`

A result returned by [`SQLiteStatement.executeAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executeasyncparams).

Example

The result includes the [`lastInsertRowId`](https://www.sqlite.org/c3ref/last_insert_rowid.html) and [`changes`](https://www.sqlite.org/c3ref/changes.html) properties. You can get the information from the write operations.

```
const statement = await db.prepareAsync('INSERT INTO test (value) VALUES (?)');
try {
  const result = await statement.executeAsync(101);
  console.log('lastInsertRowId:', result.lastInsertRowId);
  console.log('changes:', result.changes);
} finally {
  await statement.finalizeAsync();
}
```

Example

The result implements the [`AsyncIterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/asyncIterator) interface, so you can use it in `for await...of` loops.

```
const statement = await db.prepareAsync('SELECT value FROM test WHERE value > ?');
try {
  const result = await statement.executeAsync<{ value: number }>(100);
  for await (const row of result) {
    console.log('row value:', row.value);
  }
} finally {
  await statement.finalizeAsync();
}
```

Example

If your write operations also return values, you can mix all of them together.

```
const statement = await db.prepareAsync('INSERT INTO test (name, value) VALUES (?, ?) RETURNING name');
try {
  const result = await statement.executeAsync<{ name: string }>('John Doe', 101);
  console.log('lastInsertRowId:', result.lastInsertRowId);
  console.log('changes:', result.changes);
  for await (const row of result) {
    console.log('name:', row.name);
  }
} finally {
  await statement.finalizeAsync();
}
```

SQLiteExecuteAsyncResult Methods

 [`getAllAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getallasync)

Get all rows of the result set. This requires the SQLite cursor to be in its initial state. If you have already retrieved rows from the result set, you need to reset the cursor first by calling [`resetAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#resetasync). Otherwise, an error will be thrown.

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<T[]>`

 [`getFirstAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getfirstasync)

Get the first row of the result set. This requires the SQLite cursor to be in its initial state. If you have already retrieved rows from the result set, you need to reset the cursor first by calling [`resetAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#resetasync). Otherwise, an error will be thrown.

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<null | T>`

 [`resetAsync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#resetasync)

Reset the prepared statement cursor. This will call the [`sqlite3_reset()`](https://www.sqlite.org/c3ref/reset.html) C function under the hood.

Returns:

`[Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void>`

SQLiteExecuteAsyncResult Properties

|Name|Type|Description|
|---|---|---|
|**changes**|`number`|The number of rows affected. Returned from the [`sqlite3_changes()`](https://www.sqlite.org/c3ref/changes.html) function.|
|**lastInsertRowId**|`number`|The last inserted row ID. Returned from the [`sqlite3_last_insert_rowid()`](https://www.sqlite.org/c3ref/last_insert_rowid.html) function.|

  

 [`SQLiteExecuteSyncResult`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteexecutesyncresult)

Extends: `[IterableIterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator)<T>`

A result returned by [`SQLiteStatement.executeSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#executesyncparams).

> **Note:** Running heavy tasks with this function can block the JavaScript thread and affect performance.

Example

The result includes the [`lastInsertRowId`](https://www.sqlite.org/c3ref/last_insert_rowid.html) and [`changes`](https://www.sqlite.org/c3ref/changes.html) properties. You can get the information from the write operations.

```
const statement = db.prepareSync('INSERT INTO test (value) VALUES (?)');
try {
  const result = statement.executeSync(101);
  console.log('lastInsertRowId:', result.lastInsertRowId);
  console.log('changes:', result.changes);
} finally {
  statement.finalizeSync();
}
```

Example

The result implements the [`Iterator`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Iterator) interface, so you can use it in `for...of` loops.

```
const statement = db.prepareSync('SELECT value FROM test WHERE value > ?');
try {
  const result = statement.executeSync<{ value: number }>(100);
  for (const row of result) {
    console.log('row value:', row.value);
  }
} finally {
  statement.finalizeSync();
}
```

Example

If your write operations also return values, you can mix all of them together.

```
const statement = db.prepareSync('INSERT INTO test (name, value) VALUES (?, ?) RETURNING name');
try {
  const result = statement.executeSync<{ name: string }>('John Doe', 101);
  console.log('lastInsertRowId:', result.lastInsertRowId);
  console.log('changes:', result.changes);
  for (const row of result) {
    console.log('name:', row.name);
  }
} finally {
  statement.finalizeSync();
}
```

SQLiteExecuteSyncResult Methods

 [`getAllSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getallsync)

Get all rows of the result set. This requires the SQLite cursor to be in its initial state. If you have already retrieved rows from the result set, you need to reset the cursor first by calling [`resetSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#resetsync). Otherwise, an error will be thrown.

Returns:

`T[]`

 [`getFirstSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#getfirstsync)

Get the first row of the result set. This requires the SQLite cursor to be in its initial state. If you have already retrieved rows from the result set, you need to reset the cursor first by calling [`resetSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#resetsync). Otherwise, an error will be thrown.

Returns:

`null | T`

 [`resetSync()`](https://docs.expo.dev/versions/latest/sdk/sqlite/#resetsync)

Reset the prepared statement cursor. This will call the [`sqlite3_reset()`](https://www.sqlite.org/c3ref/reset.html) C function under the hood.

Returns:

`void`

SQLiteExecuteSyncResult Properties

|Name|Type|Description|
|---|---|---|
|**changes**|`number`|The number of rows affected. Returned from the [`sqlite3_changes()`](https://www.sqlite.org/c3ref/changes.html) function.|
|**lastInsertRowId**|`number`|The last inserted row ID. Returned from the [`sqlite3_last_insert_rowid()`](https://www.sqlite.org/c3ref/last_insert_rowid.html) function.|

  

 [`SQLiteOpenOptions`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteopenoptions)

Options for opening a database.

SQLiteOpenOptions Properties

|Name|Type|Description|
|---|---|---|
|**enableCRSQLite**  <br>(optional)|`boolean`|Whether to enable the CR-SQLite extension.<br><br>Default: `false`|
|**enableChangeListener**  <br>(optional)|`boolean`|Whether to call the [`sqlite3_update_hook()`](https://www.sqlite.org/c3ref/update_hook.html) function and enable the `onDatabaseChange` events. You can later subscribe to the change events by [`addDatabaseChangeListener`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteadddatabasechangelistenerlistener).<br><br>Default: `false`|
|**useNewConnection**  <br>(optional)|`boolean`|Whether to create new connection even if connection with the same database name exists in cache.<br><br>Default: `false`|

  

 [`SQLiteProviderAssetSource`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteproviderassetsource)

SQLiteProviderAssetSource Properties

|Name|Type|Description|
|---|---|---|
|**assetId**|`number`|The asset ID returned from the `require()` call.|
|**forceOverwrite**  <br>(optional)|`boolean`|Force overwrite the local database file even if it already exists.<br><br>Default: `false`|

  

 [`SQLiteRunResult`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliterunresult)

A result returned by [`SQLiteDatabase.runAsync`](https://docs.expo.dev/versions/latest/sdk/sqlite/#runasyncsource-params) or [`SQLiteDatabase.runSync`](https://docs.expo.dev/versions/latest/sdk/sqlite/#runsyncsource-params).

SQLiteRunResult Properties

|Name|Type|Description|
|---|---|---|
|**changes**|`number`|The number of rows affected. Returned from the [`sqlite3_changes()`](https://www.sqlite.org/c3ref/changes.html) function.|
|**lastInsertRowId**|`number`|The last inserted row ID. Returned from the [`sqlite3_last_insert_rowid()`](https://www.sqlite.org/c3ref/last_insert_rowid.html) function.|

  

 [Types](https://docs.expo.dev/versions/latest/sdk/sqlite/#types)

 [`DatabaseChangeEvent`](https://docs.expo.dev/versions/latest/sdk/sqlite/#databasechangeevent)

The event payload for the listener of [`addDatabaseChangeListener`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqliteadddatabasechangelistenerlistener)

|Name|Type|Description|
|---|---|---|
|**databaseFilePath**|`string`|The absolute file path to the database.|
|**databaseName**|`string`|The database name. The value would be `main` by default and other database names if you use `ATTACH DATABASE` statement.|
|**rowId**|`number`|The changed row ID.|
|**tableName**|`string`|The table name.|

 [`SQLiteBindParams`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindparams)

Literal Type: multiple types

Acceptable values are: `Record<string, [SQLiteBindValue](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue)>`

 [`SQLiteBindValue`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue)

Literal Type: multiple types

Bind parameters to the prepared statement. You can either pass the parameters in the following forms:

Example

A single array for unnamed parameters.

```
const statement = await db.prepareAsync('SELECT * FROM test WHERE value = ? AND intValue = ?');
const result = await statement.executeAsync(['test1', 789]);
const firstRow = await result.getFirstAsync();
```

Example

Variadic arguments for unnamed parameters.

```
const statement = await db.prepareAsync('SELECT * FROM test WHERE value = ? AND intValue = ?');
const result = await statement.executeAsync('test1', 789);
const firstRow = await result.getFirstAsync();
```

Example

A single object for [named parameters](https://www.sqlite.org/lang_expr.html)

We support multiple named parameter forms such as `:VVV`, `@VVV`, and `$VVV`. We recommend using `$VVV` because JavaScript allows using `$` in identifiers without escaping.

```
const statement = await db.prepareAsync('SELECT * FROM test WHERE value = $value AND intValue = $intValue');
const result = await statement.executeAsync({ $value: 'test1', $intValue: 789 });
const firstRow = await result.getFirstAsync();
```

Acceptable values are: `string` | `number` | `null` | `boolean` | `Uint8Array`

 [`SQLiteVariadicBindParams`](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitevariadicbindparams)

Type: `[SQLiteBindValue[]](https://docs.expo.dev/versions/latest/sdk/sqlite/#sqlitebindvalue)`

## Padding en Android

expo-navigation-bar
[NavigationBar - Expo Documentation](https://docs.expo.dev/versions/latest/sdk/navigation-bar/)







