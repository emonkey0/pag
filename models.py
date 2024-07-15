from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, LargeBinary, Boolean, Numeric, SmallInteger, Text, BigInteger, Float, VARBINARY
from sqlalchemy.orm import relationship
from app.config.db import Base

class ChequesTransito(Base):
    __tablename__ = 'ChequesTransito'
    idChequeTransito = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCuentaBanco = Column(Integer, nullable=False)
    NumeroCheque = Column(String(50), nullable=False)
    Importe = Column(Numeric(16, 2), nullable=False)
    Fecha = Column(DateTime, nullable=False)
    Cobrado = Column(SmallInteger, nullable=False)
    NombreBeneficiario = Column(String(100), nullable=False)
    FechaCobro = Column(DateTime)
    RFCBeneficiario = Column(String(13), nullable=False)
    app = Column(Integer)

class RestaurantCobrosAPP(Base):
    __tablename__ = 'RestaurantCobrosAPP'
    idRestaurantCobro = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCuenta = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    Importe = Column(Numeric(18, 2), nullable=False)
    NumeroDocumento = Column(String(50))
    Observaciones = Column(String(50))

class FacturaComisionista(Base):
    __tablename__ = 'FacturaComisionista'
    idFacturaComisionista = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComisionista = Column(Integer, nullable=False)
    idFactura = Column(Integer, nullable=False)
    MontoOriginal = Column(Numeric(18, 6), nullable=False)
    MontoBase = Column(Numeric(18, 6), nullable=False)
    PorcentajeComision = Column(Numeric(18, 4), nullable=False)
    ImporteComision = Column(Numeric(18, 2), nullable=False)
    Comentarios = Column(String(250))
    idUsuario = Column(Integer, nullable=False)
    idComisionista2 = Column(Integer)
    MontoBase2 = Column(Numeric(18, 6))
    PorcentajeComision2 = Column(Numeric(18, 4))
    ImporteComision2 = Column(Numeric(18, 2))
    Comentarios2 = Column(String(250))
    idComisionista3 = Column(Integer)
    MontoBase3 = Column(Numeric(18, 6))
    PorcentajeComision3 = Column(Numeric(18, 4))
    ImporteComision3 = Column(Numeric(18, 2))
    Comentarios3 = Column(String(250))
    idComisionista4 = Column(Integer)
    MontoBase4 = Column(Numeric(18, 6))
    PorcentajeComision4 = Column(Numeric(18, 4))
    ImporteComision4 = Column(Numeric(18, 2))
    Comentarios4 = Column(String(250))
    idComisionista5 = Column(Integer)
    MontoBase5 = Column(Numeric(18, 6))
    PorcentajeComision5 = Column(Numeric(18, 4))
    ImporteComision5 = Column(Numeric(18, 2))
    Comentarios5 = Column(String(250))

class ComprasDetalle(Base):
    __tablename__ = 'ComprasDetalle'
    idCompraDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCompra = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Cantidad = Column(Numeric(18, 4), nullable=False)
    DescuentoDetalle = Column(Numeric(18, 6))
    PrecioCompra = Column(Numeric(18, 6), nullable=False)
    IvaDetalleCompra = Column(Numeric(18, 6))
    ImporteCompra = Column(Numeric(18, 6))
    IEPSDetalleCompra = Column(Numeric(18, 6))
    ExistenciaFinal = Column(Numeric(18, 4))
    idProductoSeries = Column(String(500))
    idProductoTallas = Column(String(500))
    PorcientoUtilidad = Column(Numeric(14, 6))
    ObservacionesComprasDetalle = Column(String(1500))
    PrecioVentaEnClave = Column(String(10))
    Procesado = Column(Integer)
    DescuentoComercialDetalle = Column(Numeric(18, 2))
    RetIVACompra = Column(Numeric(14, 6))
    PorcientoRetIVACompra = Column(Numeric(14, 6))
    ISRCompra = Column(Numeric(14, 6))
    PorcientoISRCompra = Column(Numeric(14, 6))
    Surtido = Column(Numeric(18, 6))

class SERVICIOS_Carrier(Base):
    __tablename__ = 'SERVICIOS_Carrier'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idCarrier = Column(Integer, nullable=False)
    Nombre = Column(String(500))
    rutaLogo = Column(String(500))

class FacturasComplementoPagos(Base):
    __tablename__ = 'FacturasComplementoPagos'
    idComplementoPago = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    idFormaPago = Column(String(10), nullable=False)
    Moneda = Column(String(10), nullable=False)
    FechaPago = Column(DateTime)
    NumOperacion = Column(String(50))
    Monto = Column(Numeric(18, 6))
    TipoCambio = Column(Numeric(18, 6))
    RfcEmisorCtaOrd = Column(String(13))
    NomBancoOrdExt = Column(String(300), nullable=False)
    CtaOrdenante = Column(String(50))
    RfcEmisorCtaBen = Column(String(13))
    CtaBeneficiario = Column(String(50))
    TipoCadenaPago = Column(String(2))
    CertPago = Column(String(-1))
    CadPago = Column(String(-1))
    SelloPago = Column(String(-1))
    TotalTrasladosBaseIVA0 = Column(Numeric(18, 2))
    TotalTrasladosImpuestoIVA0 = Column(Numeric(18, 2))
    TotalTrasladosBaseIVA8 = Column(Numeric(18, 2))
    TotalTrasladosImpuestoIVA8 = Column(Numeric(18, 2))
    TotalTrasladosBaseIVA16 = Column(Numeric(18, 2))
    TotalTrasladosImpuestoIVA16 = Column(Numeric(18, 2))
    TotalTrasladosBaseIVAExento = Column(Numeric(18, 2))
    TotalRetencionesISR = Column(Numeric(18, 2))
    TotalRetencionesIVA = Column(Numeric(18, 2))
    MontoTotalPagos = Column(Numeric(18, 2))

class EmpresaFTP(Base):
    __tablename__ = 'EmpresaFTP'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idEmpresa = Column(Integer, nullable=False)
    Usuario = Column(String(500), nullable=False)
    Contrasena = Column(String(50), nullable=False)
    RutaFTP = Column(String(500))

class MS_ServicioClienteDetalle(Base):
    __tablename__ = 'MS_ServicioClienteDetalle'
    idServicioClienteDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idServicioCliente = Column(Integer)
    idServicio = Column(Integer)
    Cantidad = Column(Integer)

class sysdiagrams(Base):
    __tablename__ = 'sysdiagrams'
    name = Column(String(128), nullable=False)
    principal_id = Column(Integer, nullable=False)
    diagram_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    version = Column(Integer)
    definition = Column(VARBINARY)

class Anticipos(Base):
    __tablename__ = 'Anticipos'
    idAnticipo = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCotizacion = Column(Integer, nullable=False)
    idTipoOperacion = Column(Integer)
    idBanco = Column(Integer)
    Fecha = Column(DateTime, nullable=False)
    Cantidad = Column(Numeric(18, 2), nullable=False)
    NumeroDocumento = Column(String(50))
    idUsuario = Column(Integer)
    Observaciones = Column(String(100))
    idBancoOrigen = Column(Integer)
    FechaCaptura = Column(DateTime)
    idFormaPago = Column(String(19))
    idCuentaBanco = Column(Integer)

class PedidoViaje(Base):
    __tablename__ = 'PedidoViaje'
    idPedidoViaje = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idPedido = Column(Integer, nullable=False)
    idUnidad = Column(Integer, nullable=False)
    Origen = Column(String(100), nullable=False)
    Destino = Column(String(100), nullable=False)
    FechaViaje = Column(DateTime, nullable=False)

class ClienteAccesoGYM(Base):
    __tablename__ = 'ClienteAccesoGYM'
    idAcceso = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCliente = Column(Integer)
    fecha = Column(DateTime)

class TipoProductoDetalle(Base):
    __tablename__ = 'TipoProductoDetalle'
    idTipoProductoDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idTipoProducto = Column(Integer, nullable=False)
    TipoProductoDetalle = Column(String(50), nullable=False)
    imagenTipoProductoDetalle = Column(LargeBinary)

class NOTARIA_TipoInmueble(Base):
    __tablename__ = 'NOTARIA_TipoInmueble'
    idTipoInmueble = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveTipoInmueble = Column(String(2), nullable=False)
    TipoInmueble = Column(String(50), nullable=False)

class AjusteExistencias(Base):
    __tablename__ = 'AjusteExistencias'
    idAjuste = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    Observaciones = Column(String(100), nullable=False)
    Operacion = Column(Integer, nullable=False)
    Cantidad = Column(Numeric(14, 4), nullable=False)
    idUsuario = Column(Integer, nullable=False)
    ExistenciaFinal = Column(Numeric(14, 4))
    app = Column(Integer)

class NOMINA_MovimientosIncapacidad(Base):
    __tablename__ = 'NOMINA_MovimientosIncapacidad'
    idNominaIncapacidad = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idNominaMovimiento = Column(Integer, nullable=False)
    DiasIncapacidad = Column(Numeric(18, 6), nullable=False)
    TipoIncapacidad = Column(String(3), nullable=False)
    ConceptoIncapacidad = Column(String(50), nullable=False)
    DescuentoIncapacidad = Column(Numeric(18, 6), nullable=False)

class ProductosCostos(Base):
    __tablename__ = 'ProductosCostos'
    idProductoCosto = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Importe = Column(Numeric(14, 2))
    idTipoGasto = Column(Integer)

class Ticket(Base):
    __tablename__ = 'Ticket'
    idTicketSoporte = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCliente = Column(Integer, nullable=False)
    FechaApertura = Column(DateTime, nullable=False)
    FechaCierre = Column(DateTime)
    ComentarioCierre = Column(String(500))
    idUsuarioRecibe = Column(Integer, nullable=False)
    idUsuarioRealiza = Column(Integer)
    NumeroTicket = Column(Integer, nullable=False)
    Descripcion = Column(String(500), nullable=False)
    Prioridad = Column(String(1), nullable=False)
    idUsuarioAsignado = Column(Integer)
    Estatus = Column(String(1), nullable=False)

class FacturasComplementoPagosDetalle(Base):
    __tablename__ = 'FacturasComplementoPagosDetalle'
    idComplementoPagoDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoPago = Column(Integer, nullable=False)
    idFacturaRelacionada = Column(Integer)
    UUID = Column(String(50), nullable=False)
    Serie = Column(String(50))
    Folio = Column(String(50))
    MonedaDR = Column(String(3))
    TipoCambioDR = Column(Numeric(18, 6))
    idMetodoDePagoDR = Column(String(10))
    NumParcialidad = Column(Integer)
    ImpSaldoAnt = Column(Numeric(18, 6))
    ImpPagado = Column(Numeric(18, 6))
    ImpSaldoInsoluto = Column(Numeric(18, 6))
    ObjetoImpDR = Column(String(2))
    FactorPago = Column(Numeric(18, 10))

class CartaPorte_c_TipoPermiso(Base):
    __tablename__ = 'CartaPorte_c_TipoPermiso'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClavePermiso = Column(String(6), nullable=False)
    ClaveTransporte = Column(String(2))
    DescripcionPermiso = Column(String(500))

class EntidadFederativa(Base):
    __tablename__ = 'EntidadFederativa'
    idEntidadFederativa = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveEntidadFederativa = Column(String(2), nullable=False)
    EntidadFederativa = Column(String(50), nullable=False)

class SERVICIOS_Recargas(Base):
    __tablename__ = 'SERVICIOS_Recargas'
    idRecarga = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Producto = Column(String(500), nullable=False)
    Total = Column(Numeric(18, 2), nullable=False)
    Referencia = Column(String(50), nullable=False)
    Recibido = Column(Numeric(18, 2))
    Cambio = Column(Numeric(18, 2))
    idFormaPago = Column(String(2))
    Comision = Column(Numeric(18, 2))
    Estatus = Column(String(500))
    idUsuario = Column(Integer)

class TipoUsuarios(Base):
    __tablename__ = 'TipoUsuarios'
    idTipoUsuario = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    TipoUsuario = Column(String(50), nullable=False)

class TipoCambio(Base):
    __tablename__ = 'TipoCambio'
    idTipoCambio = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    FechaTipoCambio = Column(DateTime, nullable=False)
    TipoCambio = Column(Numeric(18, 6), nullable=False)

class Checador(Base):
    __tablename__ = 'Checador'
    idChecador = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idUsuario = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    TipoOperacion = Column(String(2), nullable=False)

class CartaPorte_c_TipoEstacion(Base):
    __tablename__ = 'CartaPorte_c_TipoEstacion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveTipoEstacion = Column(String(2), nullable=False)
    DescripcionTipoEstacion = Column(String(500))

class CatalogoUsoCFDi(Base):
    __tablename__ = 'CatalogoUsoCFDi'
    idUsoCFDi = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveUsoCFDi = Column(String(4), nullable=False)
    UsoCFDi = Column(String(100), nullable=False)
    PersonaFisica = Column(Integer, nullable=False)
    PersonaMoral = Column(Integer, nullable=False)

class ProcesoTempladora(Base):
    __tablename__ = 'ProcesoTempladora'
    idProcesoTempladora = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveProcesoTempladora = Column(String(20), nullable=False)
    DescripcionProcesoTempladora = Column(String(500))
    Color = Column(Integer)

class ConfiguracionComisiones(Base):
    __tablename__ = 'ConfiguracionComisiones'
    idConfigComisiones = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    RangoInicial = Column(Integer)
    RangoFinal = Column(Integer)
    PorcientoComision = Column(Numeric(18, 2))

class FacturasNotaria_DescInmueble(Base):
    __tablename__ = 'FacturasNotaria_DescInmueble'
    idDescripcionInmueble = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    TipoInmueble = Column(String(2), nullable=False)
    Calle = Column(String(150), nullable=False)
    NoExterior = Column(String(55))
    NoInterior = Column(String(30))
    Colonia = Column(String(100))
    Localidad = Column(String(100))
    Referencia = Column(String(100))
    Municipio = Column(String(100), nullable=False)
    Estado = Column(String(2), nullable=False)
    Pais = Column(String(3), nullable=False)
    CodigoPostal = Column(String(5), nullable=False)

class PagosComisiones(Base):
    __tablename__ = 'PagosComisiones'
    idPagoComision = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFacturaComision = Column(Integer, nullable=False)
    idTipoOperacion = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    Cantidad = Column(Numeric(18, 2), nullable=False)
    NumeroDocumento = Column(String(50))
    idUsuario = Column(Integer)
    idBanco = Column(Integer)
    idCuentaBanco = Column(Integer)
    RutaComprobante = Column(String(1000))

class CartaPorte_c_Operadores(Base):
    __tablename__ = 'CartaPorte_c_Operadores'
    idOperador = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    RFCCatalogoOperador = Column(String(15))
    NombreCatalogoOperador = Column(String(254))
    NumRegIdTribCatalogoOperador = Column(String(40))
    ResidenciaFiscalCatalogoOperador = Column(String(5))
    CalleCatalogoOperador = Column(String(100))
    NumeroExteriorCatalogoOperador = Column(String(50))
    NumeroInteriorCatalogoOperador = Column(String(50))
    ColoniaCatalogoOperador = Column(String(120))
    LocalidadCatalogoOperador = Column(String(120))
    ReferenciaCatalogoOperador = Column(String(250))
    MunicipioCatalogoOperador = Column(String(120))
    EstadoCatalogoOperador = Column(String(30))
    PaisCatalogoOperador = Column(String(5))
    CodigoPostalCatalogoOperador = Column(String(12))
    NumLicenciaCatalogoOperador = Column(String(16))

class TipoDocumento(Base):
    __tablename__ = 'TipoDocumento'
    idTipoDocumento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    TipoDocumento = Column(String(50), nullable=False)
    EsCFD = Column(Integer, nullable=False)
    TipoComprobante = Column(String(20), nullable=False)

class UsuarioPermisos(Base):
    __tablename__ = 'UsuarioPermisos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idUsuario = Column(Integer, nullable=False)
    tagMenu = Column(Integer, nullable=False)

class SERVICIOS_RecargaDetalle(Base):
    __tablename__ = 'SERVICIOS_RecargaDetalle'
    idRecargaDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idRecarga = Column(Integer, nullable=False)
    TransID = Column(String(50), nullable=False)
    Fecha = Column(DateTime)
    Carrier = Column(String(50))
    Telefono = Column(String(50))
    Folio = Column(String(50))
    Estatus = Column(String(500))
    Monto = Column(Numeric(18, 2))
    Cargo = Column(Numeric(18, 2))
    Abono = Column(Numeric(18, 2))
    Via = Column(String(50))
    Region = Column(String(50))
    Timeout = Column(String(50))
    IP = Column(String(50))
    Bolsa = Column(String(50))
    SaldoFinal = Column(Numeric(18, 2))
    Comision = Column(Numeric(18, 2))
    Mensaje = Column(String(100))

class ConteoFisicoDetalle(Base):
    __tablename__ = 'ConteoFisicoDetalle'
    idConteoFisicoDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idConteo = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    ExistenciaAnterior = Column(Numeric(18, 6), nullable=False)
    ConteoFisico = Column(Numeric(18, 6), nullable=False)
    CostoSinImpuestos = Column(Numeric(18, 6))
    PrecioVentaSinImpuestos = Column(Numeric(18, 6))

class UsuariosLog(Base):
    __tablename__ = 'UsuariosLog'
    idUsuarioLog = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idUsuario = Column(Integer, nullable=False)
    Accion = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)

class CartaPorte_c_TipoEmbalaje(Base):
    __tablename__ = 'CartaPorte_c_TipoEmbalaje'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveTipoEmbalaje = Column(String(5), nullable=False)
    DescripcionEmbalaje = Column(String(500))

class MetodoPago33(Base):
    __tablename__ = 'MetodoPago33'
    idMetodoPago = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveMetodoPago = Column(String(3))
    MetodoPago = Column(String(100))

class CobranzaBitacora(Base):
    __tablename__ = 'CobranzaBitacora'
    idCobranzaBitacora = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    Observaciones = Column(String(250), nullable=False)
    idUsuario = Column(Integer, nullable=False)

class MovimientosTimbresNomina(Base):
    __tablename__ = 'MovimientosTimbresNomina'
    idMovimientoTimbreNomina = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresaTimbre = Column(Integer, nullable=False)
    idNominaMovimiento = Column(Integer, nullable=False)
    UUID = Column(String(50))
    Estatus = Column(String(1), nullable=False)
    Fecha = Column(DateTime, nullable=False)

class Paises(Base):
    __tablename__ = 'Paises'
    idPais = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClavePais = Column(String(3), nullable=False)
    Pais = Column(String(100), nullable=False)

class ProductosDetalle(Base):
    __tablename__ = 'ProductosDetalle'
    idProductoDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Serie = Column(String(50))
    Lote = Column(String(50))
    Caducidad = Column(DateTime)
    ExistenciaDetalle = Column(Numeric(14, 4))
    Activo = Column(Integer, nullable=False)
    idFactura = Column(Integer)
    idCompra = Column(Integer)
    FechaCapturaSerie = Column(DateTime)
    AplicaPromocion = Column(Integer)

class CartaPorte_c_TipoDeServicio(Base):
    __tablename__ = 'CartaPorte_c_TipoDeServicio'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveTipoServicio = Column(String(4), nullable=False)
    DescripcionTipoServicio = Column(String(500))

class FormaPago33(Base):
    __tablename__ = 'FormaPago33'
    idFormaPago = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveFormaPago = Column(String(2), nullable=False)
    FormaPago = Column(String(100), nullable=False)

class DXDescargado(Base):
    __tablename__ = 'DXDescargado'
    idDXDescargado = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    UUID = Column(String(50))
    FechaTimbrado = Column(String(30))
    TipoDeComprobante = Column(String(1))
    FormaPago = Column(String(10))
    MetodoPago = Column(String(10))
    CondicionesDePago = Column(String(1000))
    Serie = Column(String(25))
    Folio = Column(String(40))
    SubTotal = Column(Numeric(18, 6))
    Descuento = Column(Numeric(18, 6))
    Total = Column(Numeric(18, 6))
    Moneda = Column(String(10))
    RFCEmisor = Column(String(13))
    NombreEmisor = Column(String(254))
    RFCReceptor = Column(String(13))
    NombreReceptor = Column(String(254))
    UsoCFDi = Column(String(10))
    TotalTraslados = Column(Numeric(18, 6))
    TotalRetenciones = Column(Numeric(18, 6))
    TotalTrasladosLocales = Column(Numeric(18, 6))
    TotalRetencionesLocales = Column(Numeric(18, 6))
    RutaArchivo = Column(String(-1))

class Proveedor(Base):
    __tablename__ = 'Proveedor'
    idProveedor = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    CodigoProveedor = Column(String(20))
    Nombre = Column(String(300), nullable=False)
    RFC = Column(String(13), nullable=False)
    Calle = Column(String(150))
    NumeroExterior = Column(String(10))
    NumeroInterior = Column(String(10))
    Colonia = Column(String(100))
    Localidad = Column(String(100))
    Referencia = Column(String(100))
    Municipio = Column(String(100))
    Estado = Column(String(100))
    Pais = Column(String(100))
    CodigoPostal = Column(String(5))
    Contacto = Column(String(100))
    Telefonos = Column(String(100))
    email = Column(String(100))
    PaginaWeb = Column(String(100))
    CuentaContable = Column(String(20))
    idUsuario = Column(Integer)
    ClaveEstado = Column(String(3))
    ClavePais = Column(String(3))
    NombreComercial = Column(String(300))
    ContactoCompras = Column(String(300))
    DireccionComercial = Column(String(500))
    CLABE = Column(String(50))
    Banco = Column(String(100))
    Estatus = Column(String(1))
    app = Column(Integer)

class FacturasNotaria_DatosOperacion(Base):
    __tablename__ = 'FacturasNotaria_DatosOperacion'
    idDatosOperacion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    NumInstrumentoNotarial = Column(Integer, nullable=False)
    FechaInstNotarial = Column(DateTime, nullable=False)
    MontoOperacion = Column(Numeric(18, 6), nullable=False)
    SubTotal = Column(Numeric(18, 6), nullable=False)
    IVA = Column(Numeric(18, 6), nullable=False)

class CartaPorte_c_TipoCarro(Base):
    __tablename__ = 'CartaPorte_c_TipoCarro'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveTipoCarro = Column(String(4), nullable=False)
    DescripcionTipoCarro = Column(String(500))

class CatalogoTipoRelacion(Base):
    __tablename__ = 'CatalogoTipoRelacion'
    idTipoRelacion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveTipoRelacion = Column(String(2), nullable=False)
    TipoRelacion = Column(String(100), nullable=False)

class PendienteCancelacionEmitidas(Base):
    __tablename__ = 'PendienteCancelacionEmitidas'
    idPendienteCancelacionEmitidas = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    FechaEnvio = Column(DateTime, nullable=False)
    Estatus = Column(String(1), nullable=False)
    FechaRespuesta = Column(DateTime)

class NOMINA_TipoPercepcion(Base):
    __tablename__ = 'NOMINA_TipoPercepcion'
    idTipoPercepcion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveTipoPercepcion = Column(String(3), nullable=False)
    ClavePercepcion = Column(String(15))
    TipoPercepcion = Column(String(500), nullable=False)

class ObrasGasto(Base):
    __tablename__ = 'ObrasGasto'
    idObraGasto = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idObra = Column(Integer, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idCliente = Column(Integer, nullable=False)
    idEmpleado = Column(Integer)
    Folio = Column(String(50), nullable=False)
    Fecha = Column(DateTime, nullable=False)
    Total = Column(Numeric(18, 2), nullable=False)
    Observaciones = Column(String(1500))
    Estatus = Column(String(1), nullable=False)
    TotalLetras = Column(String(500), nullable=False)
    idUsuario = Column(Integer, nullable=False)
    TipoDocumento = Column(String(50))
    idEmpleadoResponsable = Column(Integer)
    OrigenDinero = Column(String(10))
    ReporteGastos = Column(String(800))

class FacturasComplementoDivisas(Base):
    __tablename__ = 'FacturasComplementoDivisas'
    idComplementoDivisas = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    TipoOperacion = Column(String(200))

class DXDescargadoDetalle(Base):
    __tablename__ = 'DXDescargadoDetalle'
    idDXDescargadoDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idDXDescargado = Column(Integer, nullable=False)
    ClaveProdServ = Column(String(8))
    NoIdentificacion = Column(String(100))
    Cantidad = Column(Numeric(18, 6))
    ClaveUnidad = Column(String(20))
    Descripcion = Column(String(1000))
    ValorUnitario = Column(Numeric(18, 6))
    Descuento = Column(Numeric(18, 6))
    Importe = Column(Numeric(18, 6))
    BaseEXENTO = Column(Numeric(18, 6))
    BaseIVA = Column(Numeric(18, 6))
    TasaIVA = Column(Numeric(18, 6))
    ImporteIVA = Column(Numeric(18, 6))
    BaseIEPS = Column(Numeric(18, 6))
    TasaIEPS = Column(Numeric(18, 6))
    ImporteIEPS = Column(Numeric(18, 6))
    BaseRetIVA = Column(Numeric(18, 6))
    TasaRetIVA = Column(Numeric(18, 6))
    ImporteRetIVA = Column(Numeric(18, 6))
    BaseRetISR = Column(Numeric(18, 6))
    TasaRetISR = Column(Numeric(18, 6))
    ImporteRetISR = Column(Numeric(18, 6))

class ProductoPaquete(Base):
    __tablename__ = 'ProductoPaquete'
    idProductoPaquete = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer, nullable=False)
    idProductoHijo = Column(Integer, nullable=False)
    Cantidad = Column(Numeric(14, 4), nullable=False)

class Empleados(Base):
    __tablename__ = 'Empleados'
    idEmpleado = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    NumeroEmpleado = Column(String(15), nullable=False)
    NombreEmpleado = Column(String(150), nullable=False)
    RFC = Column(String(13), nullable=False)
    Calle = Column(String(100))
    NumeroExterior = Column(String(50))
    NumeroInterior = Column(String(50))
    Colonia = Column(String(50))
    Localidad = Column(String(50))
    Municipio = Column(String(50))
    Estado = Column(String(50))
    Pais = Column(String(50), nullable=False)
    CodigoPostal = Column(String(50))
    CURP = Column(String(18), nullable=False)
    idTipoRegimen = Column(Integer, nullable=False)
    NumSeguridadSocial = Column(String(15))
    idDepartamento = Column(Integer)
    idBanco = Column(Integer)
    CLABE = Column(String(18))
    FechaInicioRelLaboral = Column(DateTime)
    Puesto = Column(String(100))
    idTipoContrato = Column(Integer)
    idTipoJornada = Column(Integer)
    idPeriodicidadPago = Column(Integer)
    SalarioBaseCotApor = Column(Numeric(18, 6))
    idRiesgoPuesto = Column(Integer)
    SalarioDiarioIntegrado = Column(Numeric(18, 6))
    eMail = Column(String(100))
    Estatus = Column(String(1))
    idPlantillaRecibo = Column(Integer)
    Sindicalizado = Column(String(2))
    ClaveEntFed = Column(String(3))
    ClaveEstado = Column(String(3))
    ClavePais = Column(String(3))
    RfcPatronOrigen = Column(String(13))
    RegistroPatronal = Column(String(20))

class CartaPorte_c_NumAutorizacionNaviero(Base):
    __tablename__ = 'CartaPorte_c_NumAutorizacionNaviero'
    id = Column(Integer, primary_key=True, autoincrement=True)
    NumeroDeAutorizacionNaviero = Column(String(20), nullable=False)

class FacturasComplementoComercioExteriorMercanciasObservaciones(Base):
    __tablename__ = 'FacturasComplementoComercioExteriorMercanciasObservaciones'
    idComplementoComercioExteriorMercanciasObservaciones = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    NoIdentificacion = Column(String(100), nullable=False)
    Marca = Column(String(35), nullable=False)
    Modelo = Column(String(80))
    SubModelo = Column(String(50))
    NumeroSerie = Column(String(40))

class DENTAL_OrdenesTrabajo(Base):
    __tablename__ = 'DENTAL_OrdenesTrabajo'
    idDentalOrdenTrabajo = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idCliente = Column(Integer, nullable=False)
    NumeroOrdenTrabajo = Column(String(50), nullable=False)
    NombrePaciente = Column(String(150), nullable=False)
    EdadPaciente = Column(Integer, nullable=False)
    SexoPaciente = Column(String(1), nullable=False)
    FechaInicio = Column(DateTime, nullable=False)
    TipoTrabajo = Column(String(50), nullable=False)
    NumeroUnidades = Column(Integer, nullable=False)
    FechaPruebas = Column(DateTime)
    FechaTermino = Column(DateTime)
    HacerPruebaDe = Column(String(500))
    Observaciones = Column(String(500))
    idUsuario = Column(Integer, nullable=False)

class CartaPorte_c_Municipio(Base):
    __tablename__ = 'CartaPorte_c_Municipio'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveMunicipio = Column(String(3))
    ClaveEstado = Column(String(3))
    DescripcionMunicipio = Column(String(500))

class FacturasComplementoDetallista(Base):
    __tablename__ = 'FacturasComplementoDetallista'
    idComplementoDetallista = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    NumeroPedido = Column(String(50))
    FechaPedido = Column(DateTime)
    NumeroRemision = Column(String(50))
    NumeroContraRecibo = Column(String(50))
    FechaContraRecibo = Column(DateTime)
    GLNComprador = Column(String(50))
    DptoLiverpool = Column(String(50))
    GLNVendedor = Column(String(50))
    NumeroEmisor = Column(String(50))

class Cupones(Base):
    __tablename__ = 'Cupones'
    idCupon = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idUsuario = Column(Integer, nullable=False)
    Descripcion = Column(String(50), nullable=False)
    Existencia = Column(Integer, nullable=False)
    VentaMinima = Column(Numeric(18, 6), nullable=False)
    PorcientoDescuento = Column(Numeric(18, 6), nullable=False)
    FechaAlta = Column(DateTime)
    FechaVigencia = Column(DateTime, nullable=False)
    Estatus = Column(Integer)

class NOTARIA_DatosNotario(Base):
    __tablename__ = 'NOTARIA_DatosNotario'
    idDatosNotario = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    CURP = Column(String(18), nullable=False)
    NumNotaria = Column(Integer, nullable=False)
    EntidadFederativa = Column(String(2), nullable=False)
    Adscripcion = Column(String(255))

class ObrasGastoDetalle(Base):
    __tablename__ = 'ObrasGastoDetalle'
    idObraGastoDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idObraGasto = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Identificador = Column(String(50), nullable=False)
    Modelo = Column(String(50))
    Familia = Column(String(50))
    Descripcion = Column(String(100), nullable=False)
    Importe = Column(Numeric(18, 2), nullable=False)
    Observaciones = Column(String(1500))
    idProveedor = Column(Integer)
    idFormaPago = Column(String(2))
    idTipoDocumento = Column(Integer)
    NumeroDocumento = Column(String(150))
    FechaDocumento = Column(DateTime)
    idBanco = Column(Integer)
    idCuentaBanco = Column(Integer)

class CartaPorte_c_MaterialPeligroso(Base):
    __tablename__ = 'CartaPorte_c_MaterialPeligroso'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveMaterialPeligroso = Column(String(5), nullable=False)
    DescripcionMaterialPeligroso = Column(String(500))

class TipoGasto(Base):
    __tablename__ = 'TipoGasto'
    idTipoGasto = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    TipoGasto = Column(String(50), nullable=False)
    Descripcion = Column(String(200))
    Estatus = Column(String(1))

class RET_CFDIRetencion(Base):
    __tablename__ = 'RET_CFDIRetencion'
    idCFDIRetencion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    FolioInterno = Column(Integer, nullable=False)
    SelloDigital = Column(String(-1))
    NumeroCertificado = Column(String(30))
    Certificado = Column(String(-1))
    FechaExpedicion = Column(String(30))
    ClaveRetencion = Column(String(2), nullable=False)
    DescripcionRetencion = Column(String(100))
    RFCEmisor = Column(String(15))
    NombreEmisor = Column(String(300))
    CURPEmisor = Column(String(20))
    NacionalidadReceptor = Column(String(15))
    RFCReceptor = Column(String(15))
    NombreReceptor = Column(String(300))
    CURPReceptor = Column(String(20))
    NumeroRegistroFiscalExtranjero = Column(String(20))
    MesInicial = Column(String(2), nullable=False)
    MesFinal = Column(String(2), nullable=False)
    Ejercicio = Column(Integer, nullable=False)
    MontoTotalOperacion = Column(Numeric(18, 6), nullable=False)
    MontoTotalGravado = Column(Numeric(18, 6), nullable=False)
    MontoTotalExento = Column(Numeric(18, 6), nullable=False)
    MontoTotalRetenido = Column(Numeric(18, 6), nullable=False)
    RutaXML = Column(String(500))
    UUID = Column(String(50))
    SelloSAT = Column(String(-1))
    noCertificadoSAT = Column(String(20))
    FechaTimbrado = Column(String(30))
    RutaCertificado = Column(String(500))
    CadenaOriginal = Column(String(-1))
    CadenaOriginalTFD = Column(String(-1))
    idComplemento = Column(Integer)
    CodigoBarras = Column(LargeBinary)
    Observaciones = Column(String(500))
    Estatus = Column(String(1))
    ClaveCancelacion = Column(String(2))
    FolioSustituye = Column(String(50))
    UtilidadBimestral = Column(Numeric(18, 6))
    ISRCorrespondiente = Column(Numeric(18, 6))
    DomicilioFiscalR = Column(String(10))

class PendienteCancelacionRecibidas(Base):
    __tablename__ = 'PendienteCancelacionRecibidas'
    idPendienteCancelacionRecibida = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    UUID = Column(String(50), nullable=False)
    FechaRespuesta = Column(DateTime)
    Estatus = Column(String(1), nullable=False)

class NOMINA_MovimientosCFDiRelacionados(Base):
    __tablename__ = 'NOMINA_MovimientosCFDiRelacionados'
    idNominaCFDiRelacionado = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idNominaMovimiento = Column(Integer, nullable=False)
    idNominaMovimientoRelacionada = Column(Integer)
    Folio = Column(String(50), nullable=False)
    UUID = Column(String(50), nullable=False)
    TipoRelacion = Column(String(2))

class CartaPorte_c_Localidad(Base):
    __tablename__ = 'CartaPorte_c_Localidad'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveLocalidad = Column(String(2), nullable=False)
    ClaveEstado = Column(String(3))
    DescripcionLocalidad = Column(String(500))

class CotizacionDeExtensiones(Base):
    __tablename__ = 'CotizacionDeExtensiones'
    idCotizacionExtensiones = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCliente = Column(Integer, nullable=False)
    Fecha = Column(DateTime)
    Extensionista = Column(String(100))
    FechaEntrega = Column(DateTime)
    Largo = Column(String(500))
    Gramos = Column(String(500))
    TexturaDelCabello = Column(String(500))
    EfectoDeColor = Column(String(500))
    AlturaDeDecoracion = Column(String(500))
    TonoBase = Column(String(500))
    TonoDeseado = Column(String(500))
    TamanhoDelEncapsulado = Column(String(500))
    ObservacionesGenerales = Column(String(-1))
    Presupuesto = Column(Numeric(18, 2))

class EmpresaImpuestos(Base):
    __tablename__ = 'EmpresaImpuestos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idEmpresa = Column(Integer, nullable=False)
    IVA = Column(Numeric(19, 4), nullable=False)
    RetencionISR = Column(Numeric(19, 4))
    RetencionIVA = Column(Numeric(19, 4))
    ISSH = Column(Numeric(19, 4))
    IMCD = Column(Numeric(19, 4))

class CartaPorte_c_Estaciones(Base):
    __tablename__ = 'CartaPorte_c_Estaciones'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveEstacion = Column(String(10), nullable=False)
    ClaveTransporte = Column(String(2))
    DescripcionEstacion = Column(String(500))

class Almacenes(Base):
    __tablename__ = 'Almacenes'
    idAlmacen = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    Almacen = Column(String(50), nullable=False)
    Direccion = Column(String(200))
    idEmpresaSucursal = Column(Integer)
    idZonaImpresion = Column(Integer)

class Billetes(Base):
    __tablename__ = 'Billetes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    MilCantidad = Column(Integer)
    MilTotal = Column(Numeric(18, 2))
    QuinientosCantidad = Column(Integer)
    QuinientosTotal = Column(Numeric(18, 2))
    DoscientosCantidad = Column(Integer)
    DoscientosTotal = Column(Numeric(18, 2))
    CienCantidad = Column(Integer)
    CienTotal = Column(Numeric(18, 2))
    CincuentaCantidad = Column(Integer)
    CincuentaTotal = Column(Numeric(18, 2))
    VeinteCantidad = Column(Integer)
    VeinteTotal = Column(Numeric(18, 2))
    DiezCantidad = Column(Integer)
    DiezTotal = Column(Numeric(18, 2))
    CincoCantidad = Column(Integer)
    CincoTotal = Column(Numeric(18, 2))
    DosCantidad = Column(Integer)
    DosTotal = Column(Numeric(18, 2))
    UnoCantidad = Column(Integer)
    UnoTotal = Column(Numeric(18, 2))

class EmpresaExpedicion(Base):
    __tablename__ = 'EmpresaExpedicion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idEmpresa = Column(Integer, nullable=False)
    Calle = Column(String(150))
    NumeroExterior = Column(String(10))
    NumeroInterior = Column(String(10))
    Colonia = Column(String(100))
    Localidad = Column(String(100))
    Referencia = Column(String(100))
    Municipio = Column(String(100))
    Estado = Column(String(100))
    Pais = Column(String(100))
    CodigoPostal = Column(String(5), nullable=False)

class CartaPorte_c_DerechosDePaso(Base):
    __tablename__ = 'CartaPorte_c_DerechosDePaso'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveDerechoPaso = Column(String(20), nullable=False)
    DerechoPaso = Column(String(50))
    Entre = Column(String(500))
    Hasta = Column(String(500))
    OtorgaRecibe = Column(String(20))
    Concesionario = Column(String(500))

class NOMINA_MovimientosPercepciones(Base):
    __tablename__ = 'NOMINA_MovimientosPercepciones'
    idNominaPercepcion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idNominaMovimiento = Column(Integer, nullable=False)
    TipoPercepcion = Column(String(3), nullable=False)
    ClavePercepcion = Column(String(15), nullable=False)
    ConceptoPercepcion = Column(String(500), nullable=False)
    ImporteGravadoPercepcion = Column(Numeric(18, 6), nullable=False)
    ImporteExentoPercepcion = Column(Numeric(18, 6), nullable=False)
    ObservacionesPercepcion = Column(String(150))
    ValorMercado = Column(Numeric(18, 6))
    PrecioAlOtorgarse = Column(Numeric(18, 6))
    TotalPagado = Column(Numeric(18, 6))
    NumAnosServicio = Column(Numeric(18, 6))
    UltimoSueldoMensOrd = Column(Numeric(18, 6))
    IngresoAcumulable = Column(Numeric(18, 6))
    IngresoNoAcumulable = Column(Numeric(18, 6))
    MontoDiario = Column(Numeric(18, 6))
    TotalUnaExhibicion = Column(Numeric(18, 6))
    TotalParcialidad = Column(Numeric(18, 6))
    IngresoAcumulablePension = Column(Numeric(18, 6))
    IngresoNoAcumulablePension = Column(Numeric(18, 6))

class Monedas(Base):
    __tablename__ = 'Monedas'
    idMoneda = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Descripcion = Column(String(50), nullable=False)
    Abreviatura = Column(String(10), nullable=False)
    Clave = Column(String(3))

class CotizacionDeDisenhoDeColor(Base):
    __tablename__ = 'CotizacionDeDisenhoDeColor'
    idCotizacionDisenhoColor = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCliente = Column(Integer, nullable=False)
    Fecha = Column(DateTime)
    Colorista = Column(String(100))
    EstadoActualDelCabello = Column(String(500))
    DisenhoColorDeseado = Column(String(500))
    TecnicaRealizar = Column(String(500))
    CorreccionDeTonoBase = Column(String(2))
    TonoBase = Column(String(100))
    RetoqueDeTinte = Column(String(2))
    TonoDeTinte = Column(String(100))
    CorteDeCabello = Column(String(2))
    AlturaDeDecoloracion = Column(String(500))
    TonoDeseado = Column(String(500))
    AntesDeDecoloracion = Column(String(500))
    DespuesDeDecoloracion = Column(String(500))
    ObservacionesGenerales = Column(String(-1))
    Presupuesto = Column(Numeric(18, 2))

class FacturasDetalleSerie(Base):
    __tablename__ = 'FacturasDetalleSerie'
    idFacturasDetalleSerie = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFacturaDetalle = Column(Integer, nullable=False)
    idProductoDetalle = Column(Integer, nullable=False)

class CuponesAplicado(Base):
    __tablename__ = 'CuponesAplicado'
    idCuponAplicado = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCupon = Column(Integer, nullable=False)
    idFactura = Column(Integer, nullable=False)

class EmpresaCertificado(Base):
    __tablename__ = 'EmpresaCertificado'
    idEmpresaCertificado = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    RutaCertificado = Column(String(300))
    RutaLlavePrivada = Column(String(300))
    VigenciaDesde = Column(String(10))
    VigenciaHasta = Column(String(10))
    AvisoVencimiento = Column(Integer)
    Serie = Column(String(300))
    Certificado = Column(String(-1))
    LlavePrivada = Column(String(-1))
    Contrasea = Column(String(100))

class CartaPorte_c_CveTransporte(Base):
    __tablename__ = 'CartaPorte_c_CveTransporte'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveTransporte = Column(String(2), nullable=False)
    DescripcionTransporte = Column(String(500))

class CatalogoServiciosDCS(Base):
    __tablename__ = 'CatalogoServiciosDCS'
    idCatalogoServiciosDCS = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ServiciosDCS = Column(String(100), nullable=False)
    Cantidad = Column(Integer, nullable=False)

class MetodoPago(Base):
    __tablename__ = 'MetodoPago'
    idMetodoPago = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveMetodoPago = Column(String(2))
    MetodoPago = Column(String(100))
    Estatus = Column(String(1))

class RET_CFDiRetencionDetalle(Base):
    __tablename__ = 'RET_CFDiRetencionDetalle'
    idCFDiRetencionDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCFDiRetencion = Column(Integer, nullable=False)
    BaseImpuesto = Column(Numeric(18, 6))
    idImpuesto = Column(String(3))
    montoRetenido = Column(Numeric(18, 6), nullable=False)
    ImpuestoDescripcion = Column(String(5))
    idTipoPagoRet = Column(String(2), nullable=False)
    TipoPagoRetDescripcion = Column(String(45), nullable=False)

class CartaPorte_c_ContenedorMaritimo(Base):
    __tablename__ = 'CartaPorte_c_ContenedorMaritimo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveContenedorMaritimo = Column(String(5), nullable=False)
    DescripcionContenedorMaritimo = Column(String(500))

class ContadorBilletes(Base):
    __tablename__ = 'ContadorBilletes'
    idContadorBilletes = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idUsuario = Column(Integer, nullable=False)
    fecha = Column(DateTime)
    Total = Column(Numeric(14, 6))
    TipoOperacion = Column(String(50))
    Moneda = Column(Integer)

class TransferenciasDetalle(Base):
    __tablename__ = 'TransferenciasDetalle'
    idTransferenciaDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idTransferencia = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Cantidad = Column(Numeric(18, 4), nullable=False)
    ExistenciaFinal = Column(Numeric(18, 4))
    idProductoSeries = Column(String(500))
    idProductoTallas = Column(String(500))
    idProductoLotes = Column(String(500))

class ConsumoFinkok(Base):
    __tablename__ = 'ConsumoFinkok'
    idTimbrado = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Mes = Column(Integer, nullable=False)
    Anno = Column(Integer, nullable=False)
    RFC = Column(String(13), nullable=False)
    Cantidad = Column(Integer, nullable=False)

class Parcialidades(Base):
    __tablename__ = 'Parcialidades'
    idParcialidad = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    idTipoDocumento = Column(Integer, nullable=False)
    idFormaPago = Column(String(50), nullable=False)
    idMetodoPago = Column(String(50), nullable=False)
    Serie = Column(String(20))
    Folio = Column(String(20))
    Fecha = Column(DateTime, nullable=False)
    FechaSAT = Column(String(30), nullable=False)
    SerieCertificado = Column(String(300))
    Certificado = Column(String(-1))
    CadenaOriginal = Column(String(-1))
    CadenaOriginalTFD = Column(String(-1))
    SelloDigital = Column(String(-1))
    SubTotal = Column(Numeric(18, 6))
    ImporteIVA = Column(Numeric(18, 6), nullable=False)
    Total = Column(Numeric(18, 6))
    DatosEnvio = Column(String(500))
    Estatus = Column(String(1), nullable=False)
    FechaCancelacion = Column(DateTime)
    TotalLetras = Column(String(-1))
    RutaXML = Column(String(500))
    UUID = Column(String(50))
    SelloSAT = Column(String(-1))
    noCertificadoSAT = Column(String(20))
    FechaTimbrado = Column(String(30))
    CodigoBarras = Column(LargeBinary)
    idMoneda = Column(Integer, nullable=False)
    TipoCambio = Column(Numeric(18, 6), nullable=False)
    idUsuario = Column(Integer)
    NumCtaPago = Column(String(60))
    FolioFiscalOrig = Column(String(50))
    SerieFolioFiscalOrig = Column(String(20))
    FechaFolioFiscalOrig = Column(String(30))
    MontoFolioFiscalOrig = Column(Numeric(18, 6))
    idEmpresaFolio = Column(Integer)
    LlavePrivada = Column(String(-1))
    RutaCertificado = Column(String(300))
    idPac = Column(Integer)
    MotivoCancelacion = Column(String(200))
    idCobro = Column(Integer)

class ProductosNegados(Base):
    __tablename__ = 'ProductosNegados'
    idProductoNegado = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idPedidoCliente = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Cantidad = Column(Numeric(16, 2), nullable=False)

class ClienteServiciosRenta(Base):
    __tablename__ = 'ClienteServiciosRenta'
    idClienteServiciosRentas = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCliente = Column(Integer, nullable=False)
    idPoliza = Column(Integer, nullable=False)
    Observaciones = Column(String(250), nullable=False)
    Fecha = Column(DateTime, nullable=False)
    idUsuario = Column(Integer, nullable=False)
    idCatalogoServiciosDCS = Column(Integer)

class Polizas(Base):
    __tablename__ = 'Polizas'
    idPoliza = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    FechaInicio = Column(DateTime, nullable=False)
    RutaPDF = Column(String(1050), nullable=False)
    Estatus = Column(String(1), nullable=False)
    Numero = Column(Integer, nullable=False)
    FechaFin = Column(DateTime, nullable=False)
    Observaciones = Column(String(1000))
    idGESEM = Column(Integer)
    Periodicidad = Column(Integer)
    idTipoPoliza = Column(Integer)
    Observaciones2 = Column(String(1000))

class FacturasComplementoCartaPorteUbicacion(Base):
    __tablename__ = 'FacturasComplementoCartaPorteUbicacion'
    idComplementoCartaPorteUbicacion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorte = Column(Integer, nullable=False)
    TipoUbicacion = Column(String(10))
    IDUbicacion = Column(String(8))
    RFCRemitenteDestinatario = Column(String(15))
    NombreRemitenteDestinatario = Column(String(254))
    NumRegIdTrib = Column(String(40))
    ResidenciaFiscal = Column(String(5))
    NumEstacion = Column(String(10))
    NombreEstacion = Column(String(50))
    NavegacionTrafico = Column(String(10))
    FechaHoraSalidaLlegada = Column(String(20))
    TipoEstacion = Column(String(2))
    DistanciaRecorrida = Column(Numeric(18, 2))
    CalleUbicacion = Column(String(100))
    NumeroExteriorUbicacion = Column(String(50))
    NumeroInteriorUbicacion = Column(String(50))
    ColoniaUbicacion = Column(String(120))
    LocalidadUbicacion = Column(String(120))
    ReferenciaUbicacion = Column(String(250))
    MunicipioUbicacion = Column(String(120))
    EstadoUbicacion = Column(String(30))
    PaisUbicacion = Column(String(5))
    CodigoPostalUbicacion = Column(String(12))

class CartaPorte_c_Contenedor(Base):
    __tablename__ = 'CartaPorte_c_Contenedor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveTipoContenedor = Column(String(4), nullable=False)
    TipoContenedor = Column(String(10))
    DescripcionTipoContenedor = Column(String(200))

class TransferenciasRequisicion(Base):
    __tablename__ = 'TransferenciasRequisicion'
    idTransferenciaRequisicion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idAlmacenOrigen = Column(Integer, nullable=False)
    idAlmacenDestino = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    NumeroTransferenciaRequisicion = Column(Integer)
    Observaciones = Column(String(500))
    Estatus = Column(String(1), nullable=False)
    idUsuario = Column(Integer, nullable=False)
    idTransferencia = Column(Integer)

class NOMINA_PlantillaReciboDeduccion(Base):
    __tablename__ = 'NOMINA_PlantillaReciboDeduccion'
    idPlantillaReciboDeduccion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idPlantillaRecibo = Column(Integer, nullable=False)
    TipoDeduccion = Column(String(3), nullable=False)
    ClaveDeduccion = Column(String(15), nullable=False)
    ConceptoDeduccion = Column(String(200), nullable=False)
    ImporteGravadoDeduccion = Column(Numeric(18, 6), nullable=False)
    ImporteExentoDeduccion = Column(Numeric(18, 6))

class RET_ComplementoDividendos(Base):
    __tablename__ = 'RET_ComplementoDividendos'
    idRetComplemento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCFDIRetencion = Column(Integer, nullable=False)
    CveTipDivOUtil = Column(String(2))
    MontISRAcredRetMexico = Column(Numeric(18, 6))
    MontISRAcredRetExtranjero = Column(Numeric(18, 6))
    MontRetExtDivExt = Column(Numeric(18, 6))
    TipoSocDistrDiv = Column(String(50))
    MontISRAcredNal = Column(Numeric(18, 6))
    MontDivAcumNal = Column(Numeric(18, 6))
    MontDivAcumExt = Column(Numeric(18, 6))
    ProporcionRem = Column(Numeric(18, 6))

class Transferencias(Base):
    __tablename__ = 'Transferencias'
    idTransferencia = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idAlmacenOrigen = Column(Integer, nullable=False)
    idAlmacenDestino = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    NumeroTransferencia = Column(Integer)
    Observaciones = Column(String(500))
    Estatus = Column(String(1), nullable=False)
    idUsuario = Column(Integer, nullable=False)
    Sucursal = Column(Integer)

class CartaPorte_c_ConfigMaritima(Base):
    __tablename__ = 'CartaPorte_c_ConfigMaritima'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveConfMaritima = Column(String(3), nullable=False)
    DescripcionConfigMaritima = Column(String(500))

class GYM_HistoricoFechaProximoPago(Base):
    __tablename__ = 'GYM_HistoricoFechaProximoPago'
    idGYM_HistoricoFechaProximoPago = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCliente = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    FechaPagoAnterior = Column(DateTime, nullable=False)
    FechaPagoNueva = Column(DateTime, nullable=False)
    idUsuario = Column(Integer, nullable=False)
    idFactura = Column(Integer)
    idEmpresa = Column(Integer, nullable=False)

class NOMINA_TipoDeduccion(Base):
    __tablename__ = 'NOMINA_TipoDeduccion'
    idTipoDeduccion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveTipoDeduccion = Column(String(3), nullable=False)
    ClaveDeduccion = Column(String(15))
    TipoDeduccion = Column(String(100), nullable=False)

class ConfiguracionPromociones(Base):
    __tablename__ = 'ConfiguracionPromociones'
    idConfigPromociones = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    Desde = Column(Numeric(18, 4), nullable=False)
    Hasta = Column(Numeric(18, 4), nullable=False)
    PorcientoDescuento = Column(Numeric(18, 4), nullable=False)
    idPrecio = Column(Integer, nullable=False)
    NombrePrecio = Column(String(50), nullable=False)
    CantidadMostrarMensaje = Column(Numeric(18, 4))

class NOMINA_PlantillaReciboPercepcion(Base):
    __tablename__ = 'NOMINA_PlantillaReciboPercepcion'
    idPlantillaReciboPercepcion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idPlantillaRecibo = Column(Integer, nullable=False)
    TipoPercepcion = Column(String(3), nullable=False)
    ClavePercepcion = Column(String(15), nullable=False)
    ConceptoPercepcion = Column(String(200), nullable=False)
    ImporteGravadoPercepcion = Column(Numeric(18, 6), nullable=False)
    ImporteExentoPercepcion = Column(Numeric(18, 6), nullable=False)

class RestaurantZonaMesas(Base):
    __tablename__ = 'RestaurantZonaMesas'
    idZona = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Nombre = Column(String(100), nullable=False)
    Estatus = Column(String(1), nullable=False)
    idApp = Column(Integer)

class CartaPorte_c_ConfigAutotransporte(Base):
    __tablename__ = 'CartaPorte_c_ConfigAutotransporte'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveAutoTransporte = Column(String(10), nullable=False)
    DescripcionAutoTransporte = Column(String(500))
    Ejes = Column(String(20))
    Llantas = Column(String(20))

class EC_PedidoArchivo(Base):
    __tablename__ = 'EC_PedidoArchivo'
    idArchivo = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idPedido = Column(Integer)
    ruta = Column(String(-1))
    nombreArchivo = Column(String(100))

class ProveedorCuenta(Base):
    __tablename__ = 'ProveedorCuenta'
    idProveedorCuenta = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProveedor = Column(Integer, nullable=False)
    CuentaContable = Column(String(20))
    CLABE = Column(String(50), nullable=False)
    Banco = Column(String(10), nullable=False)

class FacturasComplementoPagosDetalleExterno(Base):
    __tablename__ = 'FacturasComplementoPagosDetalleExterno'
    idComplementoPagoDetalleExterno = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoPago = Column(Integer)
    UUID = Column(String(50))
    Tipo = Column(String(50))
    Base = Column(Numeric(18, 6))
    Impuesto = Column(String(3))
    TipoFactor = Column(String(20))
    TasaOCuota = Column(Numeric(18, 6))
    Importe = Column(Numeric(18, 6))

class ClienteZona(Base):
    __tablename__ = 'ClienteZona'
    idClienteZona = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    ClienteZona = Column(String(100), nullable=False)
    Estatus = Column(String(1), nullable=False)

class RestaurantMeseros(Base):
    __tablename__ = 'RestaurantMeseros'
    idMesero = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Nombre = Column(String(100), nullable=False)
    Usuario = Column(String(20), nullable=False)
    Contrasea = Column(Integer, nullable=False)
    Estatus = Column(String(1), nullable=False)
    PuedeCobrar = Column(Integer)
    EditarArticulo = Column(Integer)
    EliminarArticulo = Column(Integer)
    Administrador = Column(Integer)
    PuedeImprimirCuenta = Column(Integer)

class CartaPorte_c_CodigoTransporteAereo(Base):
    __tablename__ = 'CartaPorte_c_CodigoTransporteAereo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveTransporteAereo = Column(String(5), nullable=False)
    Nacionalidad = Column(String(50))
    NombreAerolinea = Column(String(500))
    DesignadorOACI = Column(String(10))

class PagosComisiones5(Base):
    __tablename__ = 'PagosComisiones5'
    idPagoComision = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFacturaComision = Column(Integer, nullable=False)
    idTipoOperacion = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    Cantidad = Column(Numeric(18, 2), nullable=False)
    NumeroDocumento = Column(String(50))
    idUsuario = Column(Integer)
    idBanco = Column(Integer)
    idCuentaBanco = Column(Integer)
    RutaComprobante = Column(String(1000))

class NOMINA_PlantillaRecibos(Base):
    __tablename__ = 'NOMINA_PlantillaRecibos'
    idPlantillaRecibo = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    NombrePlantilla = Column(String(25), nullable=False)
    idFormaPago = Column(Integer)
    idMetodoPago = Column(String(50))

class FacturasComplementoCartaPorteTipoFigura(Base):
    __tablename__ = 'FacturasComplementoCartaPorteTipoFigura'
    idComplementoCartaPorteTipoFigura = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorte = Column(Integer, nullable=False)
    TipoFigura = Column(String(2))
    RFCFigura = Column(String(20))
    NumLicencia = Column(String(16))
    NombreFigura = Column(String(254))
    NumRegIdTribFigura = Column(String(40))
    ResidenciaFiscalFigura = Column(String(5))
    CalleFigura = Column(String(-1))
    NumeroExteriorFigura = Column(String(50))
    NumeroInteriorFigura = Column(String(50))
    ColoniaFigura = Column(String(120))
    LocalidadFigura = Column(String(120))
    ReferenciaFigura = Column(String(120))
    MunicipioFigura = Column(String(120))
    EstadoFigura = Column(String(30))
    PaisFigura = Column(String(5))
    CodigoPostalFigura = Column(String(12))

class ProductoPedaceria(Base):
    __tablename__ = 'ProductoPedaceria'
    idProductoPedaceria = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Descripcion = Column(String(1000), nullable=False)
    Largo = Column(Numeric(14, 4), nullable=False)
    Ancho = Column(Numeric(14, 4), nullable=False)
    Existencia = Column(Numeric(14, 4), nullable=False)
    Costo = Column(Numeric(14, 6))

class ClienteZonaRuta(Base):
    __tablename__ = 'ClienteZonaRuta'
    idClienteZonaRuta = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idClienteZona = Column(Integer, nullable=False)
    ClienteZonaRuta = Column(String(100), nullable=False)

class RestaurantMesas(Base):
    __tablename__ = 'RestaurantMesas'
    idMesa = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Nombre = Column(String(100), nullable=False)
    idZona = Column(Integer, nullable=False)
    Estatus = Column(String(1), nullable=False)
    CantidadPersonas = Column(Integer)

class CartaPorte_c_ClaveTipoCarga(Base):
    __tablename__ = 'CartaPorte_c_ClaveTipoCarga'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveTipoCarga = Column(String(3), nullable=False)
    DescripcionTipoCarga = Column(String(500))

class Pedidos(Base):
    __tablename__ = 'Pedidos'
    idPedido = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idProveedor = Column(Integer, nullable=False)
    NumeroPedido = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    FechaPromesa = Column(DateTime)
    Observaciones = Column(String(500))
    idUsuario = Column(Integer)
    SubTotal = Column(Numeric(18, 6))
    ImporteIVA = Column(Numeric(18, 6))
    RutaPDF = Column(String(500))
    NombreProveedor = Column(String(150))
    PorcentajeDescuento = Column(Numeric(18, 6))
    ImporteDescuento = Column(Numeric(18, 6))
    ImporteIEPS = Column(Numeric(18, 6))
    Total = Column(Numeric(18, 6))
    idAlmacen = Column(Integer)
    idCompra = Column(Integer)
    idEstatus = Column(Integer)
    idMoneda = Column(Integer)
    CantidadLetras = Column(String(250))
    Documento = Column(String(50))
    app = Column(Integer)

class MotivoDescuento(Base):
    __tablename__ = 'MotivoDescuento'
    idMotivoDescuento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    MotivoDescuento = Column(String(50), nullable=False)

class TransferenciasRequisicionDetalle(Base):
    __tablename__ = 'TransferenciasRequisicionDetalle'
    idTransferenciaRequisicionDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idTransferenciaRequisicion = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Cantidad = Column(Numeric(18, 4), nullable=False)

class RestaurantComandaDetalle(Base):
    __tablename__ = 'RestaurantComandaDetalle'
    idComandaDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComanda = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Cantidad = Column(Numeric(18, 4), nullable=False)
    Precio = Column(Numeric(18, 6), nullable=False)
    Observaciones = Column(String(1000))
    TotalDetalleSinDescuento = Column(Numeric(18, 6), nullable=False)
    PorcientoDescuentoDetalle = Column(Numeric(18, 6), nullable=False)
    DescuentoDetalle = Column(Numeric(18, 6), nullable=False)
    TotalDetalleConDescuento = Column(Numeric(18, 6), nullable=False)
    RutaImpresion = Column(String(100))
    Producto = Column(String(1000))
    esComplementoDe = Column(Integer)
    esModificadorDe = Column(Integer)
    FactorExistencia = Column(Numeric(18, 6))

class CartaPorte_c_ClaveProdSTCC(Base):
    __tablename__ = 'CartaPorte_c_ClaveProdSTCC'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveProductoSTCC = Column(String(20), nullable=False)
    DescripcionProductoSTCC = Column(String(500))

class FacturasComplementoComercioExteriorPropietario(Base):
    __tablename__ = 'FacturasComplementoComercioExteriorPropietario'
    idComplementoComercioExteriorPropietario = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoComercioExterior = Column(Integer, nullable=False)
    NumRegIdTribPropietario = Column(String(40), nullable=False)
    ResidenciaFiscalPropietario = Column(String(3), nullable=False)

class ClienteMonederoMovimientos(Base):
    __tablename__ = 'ClienteMonederoMovimientos'
    idClienteMonederoMovimiento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idClienteMonedero = Column(Integer)
    idFactura = Column(Integer)
    puntosAcumulados = Column(Numeric(18, 2))
    valorPuntos = Column(Numeric(18, 4))
    idAcumulacionPuntos = Column(Integer)
    saldoUsado = Column(Numeric(18, 2))
    fecha = Column(DateTime, nullable=False)
    Observacion = Column(String(100))
    saldoFavor = Column(Numeric(18, 2))
    idOperacionCaja = Column(Integer)

class PagosComisiones4(Base):
    __tablename__ = 'PagosComisiones4'
    idPagoComision = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFacturaComision = Column(Integer, nullable=False)
    idTipoOperacion = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    Cantidad = Column(Numeric(18, 2), nullable=False)
    NumeroDocumento = Column(String(50))
    idUsuario = Column(Integer)
    idBanco = Column(Integer)
    idCuentaBanco = Column(Integer)
    RutaComprobante = Column(String(1000))

class FacturaCartaPorteDetalle(Base):
    __tablename__ = 'FacturaCartaPorteDetalle'
    idFacturaCartaPorteDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    Remitente = Column(String(150))
    DomicilioRemitente = Column(String(150))
    RFCremitente = Column(String(15))
    Destinatario = Column(String(150))
    DomicilioDestinatario = Column(String(150))
    RFCDestinatario = Column(String(15))
    Conductor = Column(String(200))
    Placas = Column(String(100))
    OrdenCompra = Column(String(20))
    Referencia = Column(String(20))
    Partida = Column(String(20))
    Planta = Column(String(20))

class RestaurantComanda(Base):
    __tablename__ = 'RestaurantComanda'
    idComanda = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    Observaciones = Column(String(500))
    idMesero = Column(Integer, nullable=False)
    Estatus = Column(String(1))
    idMesa = Column(Integer, nullable=False)
    NumeroComanda = Column(Integer)
    TotalSinDescuento = Column(Numeric(18, 6), nullable=False)
    Descuento = Column(Numeric(18, 6), nullable=False)
    TotalConDescuento = Column(Numeric(18, 6), nullable=False)
    idCuenta = Column(Integer)
    CantidadPersonas = Column(Integer, nullable=False)
    FolioInterno = Column(Integer)

class FacturasComplementoCartaPorteTipoFiguraParteTransporte(Base):
    __tablename__ = 'FacturasComplementoCartaPorteTipoFiguraParteTransporte'
    idComplementoCartaPorteTipoFiguraParteTransporte = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorteTipoFigura = Column(Integer, nullable=False)
    ParteTransporte = Column(String(10))

class CartaPorte_c_SubTipoRem(Base):
    __tablename__ = 'CartaPorte_c_SubTipoRem'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveTipoRemolque = Column(String(6), nullable=False)
    DescripcionTipoRemolque = Column(String(500))

class FacturasComplementoComercioExteriorMercancias(Base):
    __tablename__ = 'FacturasComplementoComercioExteriorMercancias'
    idComplementoComercioExteriorMercancias = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoComercioExterior = Column(Integer, nullable=False)
    NoIdentificacion = Column(String(100), nullable=False)
    FraccionArancelaria = Column(String(50))
    CantidadAduana = Column(Numeric(18, 3))
    UnidadAduana = Column(String(50))
    ValorUnitarioAduana = Column(Numeric(18, 6))
    ValorDolares = Column(Numeric(18, 6))

class Usuarios(Base):
    __tablename__ = 'Usuarios'
    idUsuario = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    Nombre = Column(String(20), nullable=False)
    Apellido_Paterno = Column(String(20), nullable=False)
    Apellido_Materno = Column(String(20))
    NombreCompleto = Column(String(65))
    Usuario = Column(String(20), nullable=False)
    Password = Column(String(20), nullable=False)
    idTipoUsuario = Column(Integer, nullable=False)
    Estatus = Column(String(1), nullable=False)
    Fecha_Alta = Column(DateTime, nullable=False)
    Puesto = Column(String(100))
    LimiteMaximo = Column(Numeric(18, 2))
    PrecioCompra = Column(Integer)
    PtoVentaPrecio = Column(Integer)
    PtoVentaDescuento = Column(Integer)
    PtoVentaIVA = Column(Integer)
    PtoVentaIEPS = Column(Integer)
    PtoVentaRetIVA = Column(Integer)
    PtoVentaISR = Column(Integer)
    PtoVentaIMCD = Column(Integer)
    PtoVentaDescripcionImpLocal = Column(Integer)
    PtoVentaMostrarBotones = Column(Integer)
    PtoVentaAgregarProductoAutomatico = Column(Integer)
    EliminarPagos = Column(Integer)
    EliminarCobros = Column(Integer)
    ModificarProductos = Column(Integer)
    CancelarFacturas = Column(Integer)
    AgregarFamilias = Column(Integer)
    idAlmacen = Column(String(50))
    VerificarCobrosPagos = Column(Integer)
    EstatusPedaceria = Column(Integer)
    CapturaPagosCobros = Column(Integer)
    ReportesTodosUsuarios = Column(Integer)
    BotonCerrar = Column(Integer)
    HistoricoCostos = Column(Integer)
    idComisionista = Column(Integer)
    ReimprimirTicket = Column(Integer)
    ExportarExcel = Column(Integer)
    ActivarLasF = Column(Integer)
    idEmpresaAcceso = Column(String(50))
    CambiarFechaCobrosPagos = Column(Integer)
    PorUsuario = Column(Integer)
    PorHuella = Column(Integer)
    PorAmbas = Column(Integer)
    EnviaPublicidad = Column(Integer)
    PtoVentaPrecioMayorista = Column(Integer)
    EC_accesoWeb = Column(Integer)
    SoloPedidos = Column(Integer)
    PtoVentaListaPrecios = Column(Integer)
    TodosAlmacenes = Column(Integer)
    VerificaExistenciaCotizaciones = Column(Integer)
    DevolucionesF9 = Column(Integer)
    PtoVentaDescuentoPorArticulo = Column(Integer)
    PtoVentaPorDebajoCosto = Column(Integer)
    FechaNac = Column(DateTime)
    ClonarFacturas = Column(Integer)
    CorteCajaAutomatico = Column(Integer)
    CambiarVendedor = Column(Integer)
    CajaLimitada = Column(Integer)
    ModificarPreciosDeListaPorCliente = Column(Integer)
    ModificarDescuentoPorFamilia = Column(Integer)
    Folios = Column(String(50))
    NegativosCompras = Column(Integer)
    VisualizarExistencias = Column(Integer)

class TipoOperacionCaja(Base):
    __tablename__ = 'TipoOperacionCaja'
    idTipoOperacionCaja = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    OperacionCaja = Column(String(50), nullable=False)
    Multiplicaor = Column(SmallInteger, nullable=False)

class ClienteMonederoMovimientoDetalle(Base):
    __tablename__ = 'ClienteMonederoMovimientoDetalle'
    idClienteMonederoMovimientoDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idClienteMonederoMovimiento = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    cantidad = Column(Numeric(18, 6), nullable=False)
    puntosAcumulados = Column(Numeric(18, 2), nullable=False)

class NOMINA_Departamento(Base):
    __tablename__ = 'NOMINA_Departamento'
    idDepartamento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    Departamento = Column(String(50), nullable=False)

class FacturasComplementoComercioExteriorDestinatario(Base):
    __tablename__ = 'FacturasComplementoComercioExteriorDestinatario'
    idComplementoComercioExteriorDestinatario = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoComercioExterior = Column(Integer, nullable=False)
    NumRegIdTribDestinatario = Column(String(40))
    NombreDestintario = Column(String(300))
    CalleDestinatario = Column(String(100))
    EstadoDestinatario = Column(String(30))
    PaisDestinatario = Column(String(3))
    CodigoPostalDestinatario = Column(String(12))
    ColoniaDestinatario = Column(String(120))
    LocalidadDestinatario = Column(String(120))
    NumeroExteriorDestinatario = Column(String(55))
    NumeroInteriorDestinatario = Column(String(55))
    MunicipioDestinatario = Column(String(120))
    ReferenciaDestinatario = Column(String(250))

class CartaPorte_c_ParteTransporte(Base):
    __tablename__ = 'CartaPorte_c_ParteTransporte'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveParteTransporte = Column(String(4), nullable=False)
    DescripcionParteTransporte = Column(String(500))

class FacturasConstDetalle(Base):
    __tablename__ = 'FacturasConstDetalle'
    idFacturaConstDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    Descripcion = Column(String(-1))
    DescripcionConceptoUno = Column(String(80))
    DescripcionConceptoDos = Column(String(80))
    DescripcionConceptoTres = Column(String(80))
    DescripcionConceptoCuatro = Column(String(80))
    DescripcionConceptoCinco = Column(String(80))
    DescripcionConceptoSeis = Column(String(80))
    DescripcionConceptoSiete = Column(String(80))
    DescripcionConceptoOcho = Column(String(80))
    DescripcionConceptoNueve = Column(String(80))
    DescripcionConceptoDiez = Column(String(80))
    ImporteConceptoUno = Column(Numeric(18, 6))
    ImporteConceptoDos = Column(Numeric(18, 6))
    ImporteConceptoTres = Column(Numeric(18, 6))
    ImporteConceptoCuatro = Column(Numeric(18, 6))
    ImporteConceptoCinco = Column(Numeric(18, 6))
    ImporteConceptoSeis = Column(Numeric(18, 6))
    ImporteConceptoSiete = Column(Numeric(18, 6))
    ImporteConceptoOcho = Column(Numeric(18, 6))
    ImporteConceptoNueve = Column(Numeric(18, 6))
    ImporteConceptoDiez = Column(Numeric(18, 6))
    DescripcionDescuentoUno = Column(String(80))
    DescripcionDescuentoDos = Column(String(80))
    DescripcionDescuentoTres = Column(String(80))
    DescripcionDescuentoCuatro = Column(String(80))
    DescripcionDescuentoCinco = Column(String(80))
    DescripcionDescuentoSeis = Column(String(80))
    DescripcionDescuentoSiete = Column(String(80))
    DescripcionDescuentoOcho = Column(String(80))
    DescripcionDescuentoNueve = Column(String(80))
    DescripcionDescuentoDiez = Column(String(80))
    ImporteDescuentoUno = Column(Numeric(18, 6))
    ImporteDescuentoDos = Column(Numeric(18, 6))
    ImporteDescuentoTres = Column(Numeric(18, 6))
    ImporteDescuentoCuatro = Column(Numeric(18, 6))
    ImporteDescuentoCinco = Column(Numeric(18, 6))
    ImporteDescuentoSeis = Column(Numeric(18, 6))
    ImporteDescuentoSiete = Column(Numeric(18, 6))
    ImporteDescuentoOcho = Column(Numeric(18, 6))
    ImporteDescuentoNueve = Column(Numeric(18, 6))
    ImporteDescuentoDiez = Column(Numeric(18, 6))
    AlcanceLiquido = Column(Numeric(18, 6))
    NombreUno = Column(String(50))
    CargoUno = Column(String(50))
    NombreDos = Column(String(50))
    CargoDos = Column(String(50))
    NombreTres = Column(String(50))
    CargoTres = Column(String(50))
    NombreCuatro = Column(String(50))
    CargoCuatro = Column(String(50))
    NombreCinco = Column(String(50))
    CargoCinco = Column(String(50))
    NombreSeis = Column(String(50))
    CargoSeis = Column(String(50))

class PantillaFacturas(Base):
    __tablename__ = 'PantillaFacturas'
    idPlantillaFactura = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    NombrePlantillaFactura = Column(String(50), nullable=False)
    Estatus = Column(String(1), nullable=False)
    idFormaPago = Column(String(2), nullable=False)
    idMetodoPago = Column(String(3), nullable=False)
    idCondicionesPago = Column(Integer, nullable=False)
    idUsoCFDi = Column(String(4), nullable=False)

class TipoComisionista(Base):
    __tablename__ = 'TipoComisionista'
    idTipoComisionista = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    TipoComisionista = Column(String(50), nullable=False)

class FacturasComplementoComercioExterior(Base):
    __tablename__ = 'FacturasComplementoComercioExterior'
    idComplementoComercioExterior = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    MotivoTraslado = Column(String(2))
    ClaveDePedimento = Column(String(2))
    CertificadoOrigen = Column(Integer)
    NumCertificadoOrigen = Column(String(40))
    NumeroExportadorConfiable = Column(String(50))
    Incoterm = Column(String(3))
    Subdivision = Column(Integer)
    Observaciones = Column(String(300))
    TipoCambioUSD = Column(Numeric(18, 6))
    TotalUSD = Column(Numeric(18, 6))
    NumRegIdTribReceptor = Column(String(40))
    CalleReceptor = Column(String(100))
    EstadoReceptor = Column(String(30))
    PaisReceptor = Column(String(3))
    CodigoPostalReceptor = Column(String(12))
    ClaveColoniaEmisor = Column(String(50))
    ClaveLocalidadEmisor = Column(String(50))
    ClaveMunicipioEmisor = Column(String(50))
    ColoniaReceptor = Column(String(120))
    LocalidadReceptor = Column(String(120))
    NumeroExteriorReceptor = Column(String(55))
    NumeroInteriorReceptor = Column(String(55))
    MunicipioReceptor = Column(String(120))
    ReferenciaReceptor = Column(String(250))

class PagosComisiones3(Base):
    __tablename__ = 'PagosComisiones3'
    idPagoComision = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFacturaComision = Column(Integer, nullable=False)
    idTipoOperacion = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    Cantidad = Column(Numeric(18, 2), nullable=False)
    NumeroDocumento = Column(String(50))
    idUsuario = Column(Integer)
    idBanco = Column(Integer)
    idCuentaBanco = Column(Integer)
    RutaComprobante = Column(String(1000))

class ProductoPedaceriaMovimiento(Base):
    __tablename__ = 'ProductoPedaceriaMovimiento'
    idPedaceriaMovimiento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Operacion = Column(Integer, nullable=False)
    Numero = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    Observaciones = Column(String(1000), nullable=False)
    SubTotal = Column(Numeric(18, 2), nullable=False)
    IVA = Column(Numeric(18, 2), nullable=False)
    Total = Column(Numeric(18, 2), nullable=False)
    Estatus = Column(String(1), nullable=False)
    idusuario = Column(Integer, nullable=False)
    NumeroNotaVenta = Column(Integer)

class ClienteMonedero(Base):
    __tablename__ = 'ClienteMonedero'
    idClienteMonedero = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    telefono = Column(String(10), nullable=False)
    Nombre = Column(String(100), nullable=False)
    apPaterno = Column(String(100))
    apMaterno = Column(String(100))
    Correo = Column(String(50))
    Saldo = Column(Numeric(18, 2))
    fechaCreacion = Column(DateTime)
    idEmpresa = Column(Integer, nullable=False)
    anioNacimiento = Column(Integer, nullable=False)
    saldoFavor = Column(Numeric(18, 2))
    idCliente = Column(Integer)

class PedidosDetalle(Base):
    __tablename__ = 'PedidosDetalle'
    idPedidoDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idPedido = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Descripcion = Column(String(1000), nullable=False)
    Cantidad = Column(Numeric(18, 4), nullable=False)
    Precio = Column(Numeric(18, 6))
    IvaDetalle = Column(Numeric(18, 6))
    Descuento = Column(Numeric(18, 6))
    IEPSDetalle = Column(Numeric(18, 6))
    kmAnterior = Column(Numeric(18, 6))
    kmActual = Column(Numeric(18, 6))
    kmRecorridos = Column(Numeric(18, 6))
    Rendimiento = Column(Numeric(18, 6))
    ObservacionesDetalle = Column(String(250))

class CartaPorte_c_FiguraTransporte(Base):
    __tablename__ = 'CartaPorte_c_FiguraTransporte'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveFiguraTransporte = Column(String(2), nullable=False)
    DescripcionFiguraTransporte = Column(String(500))

class Hologramas(Base):
    __tablename__ = 'Hologramas'
    idHolograma = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    FechaEntrada = Column(DateTime, nullable=False)
    FolioInicial = Column(BigInteger, nullable=False)
    FolioFinal = Column(BigInteger, nullable=False)
    UltimoFolioUsado = Column(BigInteger)
    Estatus = Column(String(1), nullable=False)

class NOMINA_TipoRegimen(Base):
    __tablename__ = 'NOMINA_TipoRegimen'
    idTipoRegimen = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveTipoRegimen = Column(String(3), nullable=False)
    TipoRegimen = Column(String(150), nullable=False)

class Comisionista(Base):
    __tablename__ = 'Comisionista'
    idComisionista = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idTipoComisionista = Column(Integer)
    CodigoComisionista = Column(String(20))
    Nombre = Column(String(300), nullable=False)
    Telefonos = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    Porcentaje = Column(Numeric(18, 2), nullable=False)
    Direccion = Column(String(200))
    idUsuario = Column(Integer, nullable=False)
    idBanco = Column(Integer)
    NumeroCuenta = Column(String(20))
    CLABE = Column(String(20))
    Meta = Column(Numeric(18, 2))
    PorcientoPagoComisiones = Column(Numeric(18, 2))
    Estatus = Column(String(1))
    SueldoBase = Column(Numeric(18, 2))
    LiderUDN = Column(Integer)
    ClaveEstadoComisionista = Column(String(3))
    MunicipioComisionista = Column(String(50))
    FechaIngreso = Column(DateTime)

class ProductoPedaceriaMovimientoDetalle(Base):
    __tablename__ = 'ProductoPedaceriaMovimientoDetalle'
    idPedaceriaMovimientoDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idPedaceriaMovimiento = Column(Integer, nullable=False)
    idProductoPedaceria = Column(Integer, nullable=False)
    Cantidad = Column(Numeric(18, 4), nullable=False)
    PrecioFinal = Column(Numeric(18, 2), nullable=False)
    SubTotal = Column(Numeric(18, 2), nullable=False)
    IVA = Column(Numeric(18, 2), nullable=False)
    Total = Column(Numeric(18, 2), nullable=False)

class TicketPendiente(Base):
    __tablename__ = 'TicketPendiente'
    idTicketPendiente = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    NombreTicket = Column(String(50), nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idUsuario = Column(String(50), nullable=False)
    Facturado = Column(String(50))
    FechaSAT = Column(String(50))
    idFactura = Column(String(50))
    TipoCambio = Column(String(50))
    idTipoDocumento = Column(String(50))
    idFormaPago = Column(String(50))
    idMetodoPago = Column(String(50))
    idCondicionesPago = Column(String(50))
    idCliente = Column(String(50))
    idComisionista = Column(String(50))
    idMoneda = Column(String(50))
    CantidadLetras = Column(String(500))
    Fecha = Column(String(50))
    SubTotalSinDescuento = Column(String(50))
    Descuento = Column(String(50))
    SubTotal = Column(String(50))
    IVA = Column(String(50))
    IEPS = Column(String(50))
    Total = Column(String(50))
    Estatus = Column(String(1))
    Serie = Column(String(50))
    Folio = Column(String(50))
    Observaciones = Column(String(500))
    DesdeBuscar = Column(Integer)

class GiroComercial(Base):
    __tablename__ = 'GiroComercial'
    idGiroComercial = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    GiroComercial = Column(String(100), nullable=False)

class NOMINA_TipoContrato(Base):
    __tablename__ = 'NOMINA_TipoContrato'
    idTipoContrato = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    TipoContrato = Column(String(150), nullable=False)
    ClaveTipoContrato = Column(String(2))

class ClienteContactos(Base):
    __tablename__ = 'ClienteContactos'
    idClienteContacto = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCliente = Column(Integer, nullable=False)
    Nombre = Column(String(200), nullable=False)
    Telefono = Column(String(10))
    Correo = Column(String(200))

class PlantillaFacturaDetalle(Base):
    __tablename__ = 'PlantillaFacturaDetalle'
    idPlantillaFacturaDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idPlantillaFactura = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    IdentificadorProducto = Column(String(50))
    Cantidad = Column(Numeric(18, 4), nullable=False)
    PrecioInicial = Column(Numeric(18, 6), nullable=False)
    PrecioFinal = Column(Numeric(18, 6), nullable=False)
    SubTotalSinDescuentoDetalle = Column(Numeric(18, 6), nullable=False)
    PorcentajeDescuentoDetalle = Column(Numeric(18, 4), nullable=False)
    DescuentoDetalle = Column(Numeric(18, 6), nullable=False)
    SubTotalConDescuentoDetalle = Column(Numeric(18, 6), nullable=False)
    PorcientoIVA = Column(Numeric(18, 6), nullable=False)
    ImporteIVA = Column(Numeric(18, 6), nullable=False)
    TotalDetalle = Column(Numeric(18, 6), nullable=False)
    Observaciones = Column(String(1000))

class TicketPendienteDetalle(Base):
    __tablename__ = 'TicketPendienteDetalle'
    idTicketPendienteDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idTicketPendiente = Column(Integer, nullable=False)
    idProducto = Column(String(50))
    Identificador = Column(String(50))
    Modelo = Column(String(50))
    Producto = Column(String(5000))
    Cantidad = Column(String(50))
    Precio = Column(String(50))
    PrecioFinal = Column(String(50))
    PorcDescuento = Column(String(50))
    Descuento = Column(String(50))
    IEPS = Column(String(50))
    SubTotalSinDescuento = Column(String(50))
    SubTotal = Column(String(50))
    IVA = Column(String(50))
    Total = Column(String(50))
    UMedida = Column(String(50))
    Tara = Column(String(50))
    idProductoSeries = Column(String(50))
    idProductoLotes = Column(String(50))
    PorcientoIEPS = Column(String(50))
    PorcientoIVA = Column(String(50))
    Exento = Column(String(10))
    idProductoTallas = Column(String(50))
    esPaquete = Column(String(50))
    Placas = Column(String(50))
    FolioHolograma = Column(String(50))
    FactorExistencia = Column(String(50))
    PrecioCompra = Column(String(50))

class FacturasComplementoCartaPorteMercanciasAutoTransporte(Base):
    __tablename__ = 'FacturasComplementoCartaPorteMercanciasAutoTransporte'
    idComplementoCartaPorteMercanciasAutoTransporte = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorteMercancias = Column(Integer, nullable=False)
    PermSCT = Column(String(10), nullable=False)
    NumPermisoSCT = Column(String(50), nullable=False)
    ConfigVehicular = Column(String(10), nullable=False)
    PlacaVM = Column(String(10), nullable=False)
    AnioModeloVM = Column(String(4), nullable=False)
    SubTipoRem1 = Column(String(7))
    PlacaRemolque1 = Column(String(10))
    SubTipoRem2 = Column(String(7))
    PlacaRemolque2 = Column(String(10))
    AseguraRespCivil = Column(String(50))
    PolizaRespCivil = Column(String(30))
    AseguraMedAmbiente = Column(String(50))
    PolizaMedAmbiente = Column(String(30))
    AseguraCarga = Column(String(50))
    PolizaCarga = Column(String(30))
    PrimaSeguro = Column(Numeric(18, 2))
    PesoBrutoVehicular = Column(Numeric(18, 2))

class NOMINA_TipoJornada(Base):
    __tablename__ = 'NOMINA_TipoJornada'
    idTipoJornada = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    TipoJornada = Column(String(50), nullable=False)
    ClaveTipoJornada = Column(String(2))

class HologramasDanados(Base):
    __tablename__ = 'HologramasDanados'
    idHologramaDanado = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idHolograma = Column(Integer, nullable=False)
    FolioDanado = Column(BigInteger, nullable=False)
    Observaciones = Column(String(100), nullable=False)
    FechaCaptura = Column(DateTime)

class TipoViatico(Base):
    __tablename__ = 'TipoViatico'
    idTipoViatico = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    TipoViatico = Column(String(50), nullable=False)

class NOMINA_Movimientos(Base):
    __tablename__ = 'NOMINA_Movimientos'
    idNominaMovimiento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idEmpleado = Column(Integer, nullable=False)
    idFormaPago = Column(Integer)
    idMetodoPago = Column(String(50))
    NumeroEmpleado = Column(String(15))
    NombreEmpleado = Column(String(100))
    RFC = Column(String(13))
    Calle = Column(String(100))
    NumExterior = Column(String(50))
    NumInterior = Column(String(50))
    Colonia = Column(String(100))
    Localidad = Column(String(100))
    Municipio = Column(String(100))
    Estado = Column(String(50))
    CodigoPostal = Column(String(6))
    Pais = Column(String(50))
    eMail = Column(String(50))
    CURP = Column(String(18))
    ClaveTipoRegimen = Column(String(50))
    NumSeguridadSocial = Column(String(15))
    FechaPago = Column(DateTime)
    FechaInicialPago = Column(DateTime)
    FechaFinalPago = Column(DateTime)
    NumDiasPagados = Column(Numeric(18, 6))
    Departamento = Column(String(100))
    CLABE = Column(String(18))
    ClaveBanco = Column(String(3))
    FechaInicioRelLaboral = Column(String(10))
    Antiguedad = Column(String(50))
    Puesto = Column(String(100))
    TipoContrato = Column(String(100))
    TipoJornada = Column(String(100))
    PeriodicidadPago = Column(String(100))
    SalarioBaseCotAport = Column(Numeric(18, 6))
    ClaveRiesgoPuesto = Column(String(3))
    SalarioDiarioIntegrado = Column(Numeric(18, 6))
    Neto = Column(Numeric(18, 6))
    TotalPercepciones = Column(Numeric(18, 6))
    TotalDeducciones = Column(Numeric(18, 6))
    ISR = Column(Numeric(18, 6))
    TotalIncapacidad = Column(Numeric(18, 6))
    TotalHorasExtra = Column(Numeric(18, 6))
    Serie = Column(String(20))
    Folio = Column(String(20))
    Fecha = Column(DateTime)
    FechaSAT = Column(String(50))
    SerieCertificado = Column(String(30))
    Certificado = Column(String(-1))
    CadenaOriginal = Column(String(-1))
    CadenaOriginalTFD = Column(String(-1))
    SelloDigital = Column(String(-1))
    Estatus = Column(String(1))
    FechaCancelacion = Column(DateTime)
    TotalLetras = Column(String(1500))
    RutaXML = Column(String(1500))
    UUID = Column(String(40))
    SelloSAT = Column(String(1500))
    noCertificadoSAT = Column(String(30))
    FechaTimbrado = Column(String(30))
    CodigoBarras = Column(LargeBinary)
    LlavePrivada = Column(String(-1))
    RutaCertificado = Column(String(1500))
    Observaciones = Column(String(500))
    idNomina = Column(Integer)
    TotalOtroPago = Column(Numeric(18, 6))
    RfcPatronOrigen = Column(String(13))
    TotalSueldos = Column(Numeric(18, 6))
    TotalSeparacionIndemnizacion = Column(Numeric(18, 6))
    TotalJubilacionPensionRetiro = Column(Numeric(18, 6))
    idOrigenRecurso = Column(String(2))
    MontoRecursoPropio = Column(Numeric(18, 4))
    RFC_PAC = Column(String(13))
    TipoRelacion = Column(String(2))
    MotivoCancelacion = Column(String(1000))
    ClaveCancelacion = Column(String(2))
    FolioSustituye = Column(String(50))

class NOMINA_PeriodicidadPago(Base):
    __tablename__ = 'NOMINA_PeriodicidadPago'
    idPeriodicidadPago = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    PeriodicidadPago = Column(String(50), nullable=False)
    ClavePeriodicidadPago = Column(String(2))

class ProductoProveedor(Base):
    __tablename__ = 'ProductoProveedor'
    idProductoProveedor = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer, nullable=False)
    idProveedor = Column(Integer, nullable=False)

class CartaPorte_c_TipoMateria(Base):
    __tablename__ = 'CartaPorte_c_TipoMateria'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveTipoMateria = Column(String(2), nullable=False)
    DescripcionTipoMateria = Column(String(500))

class FacturasNotaria_DatosEnajenante(Base):
    __tablename__ = 'FacturasNotaria_DatosEnajenante'
    idDatosEnajenante = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    Nombre = Column(String(200), nullable=False)
    ApellidoPaterno = Column(String(200))
    ApellidoMaterno = Column(String(200))
    RFC = Column(String(13), nullable=False)
    CURP = Column(String(18))
    Porcentaje = Column(Numeric(18, 2))

class ProductoPromocion(Base):
    __tablename__ = 'ProductoPromocion'
    idProductoPromocion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Desde = Column(Numeric(18, 4), nullable=False)
    Hasta = Column(Numeric(18, 4), nullable=False)
    idPrecio = Column(Integer, nullable=False)
    NombrePrecio = Column(String(50), nullable=False)
    CantidadMostrarMensaje = Column(Numeric(18, 4))
    PorcientoDescuento = Column(Numeric(18, 4))
    FechaInicial = Column(DateTime)
    FechaFinal = Column(DateTime)

class CartaPorte_c_ClaveProdServCP(Base):
    __tablename__ = 'CartaPorte_c_ClaveProdServCP'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveProdServCP = Column(String(20), nullable=False)
    DescripcionClaveProdServCP = Column(String(500))
    MaterialPeligroso = Column(String(5))

class TipoObra(Base):
    __tablename__ = 'TipoObra'
    idTipoObra = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    TipoObra = Column(String(200), nullable=False)

class FacturasComplementoCartaPorteMercanciaPedimentos(Base):
    __tablename__ = 'FacturasComplementoCartaPorteMercanciaPedimentos'
    idComplementoCartaPorteMercanciaPedimento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorteMercancia = Column(Integer, nullable=False)
    Pedimento = Column(String(21), nullable=False)
    DocumentoAduanero = Column(String(2))
    IdentDocAduanero = Column(String(150))
    RFCImpo = Column(String(13))

class CartaPorte_c_SectorCOFEPRIS(Base):
    __tablename__ = 'CartaPorte_c_SectorCOFEPRIS'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveSectorCOFEPRIS = Column(String(2), nullable=False)
    DescripcionSectorCOFEPRIS = Column(String(500))

class ClienteObservaciones(Base):
    __tablename__ = 'ClienteObservaciones'
    idClienteObservaciones = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCliente = Column(Integer, nullable=False)
    Observaciones = Column(String(250), nullable=False)
    Fecha = Column(DateTime, nullable=False)
    idUsuario = Column(Integer, nullable=False)
    idCategoriaClienteObservaciones = Column(Integer)
    RutaDocumento = Column(String(1000))

class ObservacionesProcesos(Base):
    __tablename__ = 'ObservacionesProcesos'
    idObservacionesProceso = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    Observaciones = Column(String(250), nullable=False)
    Fecha = Column(DateTime, nullable=False)
    idUsuario = Column(Integer, nullable=False)

class FacturasNotaria_DatosAdquiriente(Base):
    __tablename__ = 'FacturasNotaria_DatosAdquiriente'
    idDatosAdquiriente = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    Nombre = Column(String(200), nullable=False)
    ApellidoPaterno = Column(String(200))
    ApellidoMaterno = Column(String(200))
    RFC = Column(String(13), nullable=False)
    CURP = Column(String(18))
    Porcentaje = Column(Numeric(18, 2))

class GD_ConteoFisico(Base):
    __tablename__ = 'GD_ConteoFisico'
    idConteo = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer)
    conteo = Column(Numeric(18, 4))
    fecha = Column(DateTime)
    estatus = Column(String(1))

class FacturasComplementoINE(Base):
    __tablename__ = 'FacturasComplementoINE'
    idComplementoINE = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    TipoProceso = Column(String(50))
    TipoComite = Column(String(50))
    idContabilidad = Column(String(50))
    ClaveEntidad = Column(String(50))
    Ambito = Column(String(50))
    idContabilidadEntidad = Column(String(50))

class FacturasConstDetalleDetalle(Base):
    __tablename__ = 'FacturasConstDetalleDetalle'
    idFacturaConstDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    idConceptoConst = Column(Integer, nullable=False)
    Descripcion = Column(String(-1))
    idUnidadMedida = Column(String(50), nullable=False)
    Importe = Column(Numeric(18, 6))
    AlcanceLiquido = Column(Numeric(18, 6))
    NombreUno = Column(String(50))
    CargoUno = Column(String(200))
    AutorizaUno = Column(String(200))
    NombreDos = Column(String(50))
    CargoDos = Column(String(200))
    AutorizaDos = Column(String(200))
    NombreTres = Column(String(50))
    CargoTres = Column(String(200))
    AutorizaTres = Column(String(200))
    NombreCuatro = Column(String(50))
    CargoCuatro = Column(String(200))
    AutorizaCuatro = Column(String(200))
    NombreCinco = Column(String(50))
    CargoCinco = Column(String(200))
    AutorizaCinco = Column(String(200))
    NombreSeis = Column(String(50))
    CargoSeis = Column(String(200))
    AutorizaSeis = Column(String(200))
    esImpuestoRetenido = Column(Integer)
    TasaRetenido = Column(Numeric(18, 2))
    esImpuestoTrasladado = Column(Integer)
    TasaTrasladado = Column(Numeric(18, 2))
    ClaveUnidadMedida = Column(String(100))
    ClaveProdServ = Column(String(8))
    esDescuento = Column(Integer)
    CantidadLetrasAlcanceLiquido = Column(String(500))
    PorcientoIVA = Column(Numeric(18, 6))
    PorcientoRetIVA = Column(Numeric(18, 6))
    PorcientoRetISR = Column(Numeric(18, 6))

class CartaPorte_c_RegistroISTMO(Base):
    __tablename__ = 'CartaPorte_c_RegistroISTMO'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveRegistroISTMO = Column(String(2), nullable=False)
    DescripcionRegistroISTMO = Column(String(500))

class TraspasosTempTallas(Base):
    __tablename__ = 'TraspasosTempTallas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idTraspaso = Column(Integer, nullable=False)
    idOrigen = Column(Integer)
    idDestino = Column(Integer, nullable=False)
    idTalla = Column(Integer, nullable=False)
    idColor = Column(Integer, nullable=False)
    CodigoBarras = Column(String(50))
    Cantidad = Column(Integer, nullable=False)

class Viaticos(Base):
    __tablename__ = 'Viaticos'
    idViatico = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idEmpleado = Column(Integer, nullable=False)
    Folio = Column(String(50))
    Fecha = Column(DateTime, nullable=False)
    ImporteEntregado = Column(Numeric(18, 2), nullable=False)

class TraspasosTemp(Base):
    __tablename__ = 'TraspasosTemp'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idTraspaso = Column(Integer, nullable=False)
    idOrigen = Column(Integer)
    idDestino = Column(Integer, nullable=False)
    Cantidad = Column(Integer, nullable=False)
    Tipo = Column(String(1))
    Serie = Column(String(50))

class Facturas(Base):
    __tablename__ = 'Facturas'
    idFactura = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idTipoDocumento = Column(Integer, nullable=False)
    idCliente = Column(Integer, nullable=False)
    idFormaPago = Column(String(10))
    idMetodoPago = Column(String(50))
    Serie = Column(String(20))
    Folio = Column(Integer)
    Fecha = Column(DateTime, nullable=False)
    FechaSAT = Column(String(30), nullable=False)
    SerieCertificado = Column(String(300))
    Certificado = Column(String(-1))
    CadenaOriginal = Column(String(-1))
    CadenaOriginalTFD = Column(String(-1))
    SelloDigital = Column(String(-1))
    PorcentajeDescuento = Column(Numeric(18, 4), nullable=False)
    SubTotalAntesDescuento = Column(Numeric(18, 6), nullable=False)
    ImporteDescuento = Column(Numeric(18, 6), nullable=False)
    SubTotalConDescuento = Column(Numeric(18, 6))
    ImporteIVA = Column(Numeric(18, 6), nullable=False)
    Total = Column(Numeric(18, 6))
    DatosEnvio = Column(String(500))
    Estatus = Column(String(1), nullable=False)
    FechaCancelacion = Column(DateTime)
    TotalLetras = Column(String(-1))
    ImporteIEPS = Column(Numeric(18, 6))
    ImporteRetIVA = Column(Numeric(18, 6))
    ImporteISR = Column(Numeric(18, 6))
    ImporteIMCD = Column(Numeric(18, 6))
    ImporteISSH = Column(Numeric(18, 6))
    RutaXML = Column(String(500))
    UUID = Column(String(50))
    SelloSAT = Column(String(-1))
    noCertificadoSAT = Column(String(20))
    FechaTimbrado = Column(String(30))
    CodigoBarras = Column(LargeBinary)
    Facturado = Column(Boolean, nullable=False)
    idMoneda = Column(Integer, nullable=False)
    TipoCambio = Column(Numeric(18, 6), nullable=False)
    idUsuario = Column(Integer)
    NumCtaPago = Column(String(60))
    FolioFiscalOrig = Column(String(50))
    SerieFolioFiscalOrig = Column(String(20))
    FechaFolioFiscalOrig = Column(String(30))
    MontoFolioFiscalOrig = Column(Numeric(18, 6))
    Propina = Column(Numeric(18, 6))
    idCondicionesPago = Column(Integer)
    idEmpresaFolio = Column(Integer)
    AutoUnidad = Column(String(50))
    AutoMarca = Column(String(50))
    AutoModelo = Column(String(50))
    AutoPlacas = Column(String(50))
    AutoSiniestro = Column(String(50))
    AutoPoliza = Column(String(50))
    AutoReporte = Column(String(50))
    LlavePrivada = Column(String(-1))
    RutaCertificado = Column(String(300))
    idPac = Column(Integer)
    idNotaVenta = Column(Integer)
    MotivoCancelacion = Column(String(200))
    Costo = Column(Numeric(18, 6))
    NotariaEscritura = Column(String(50))
    DescripcionRetencionUno = Column(String(50))
    ImporteRetencionUno = Column(Numeric(18, 6))
    DescripcionRetencionDos = Column(String(50))
    ImporteRetencionDos = Column(Numeric(18, 6))
    TasaRetencionUno = Column(Numeric(18, 6))
    TasaRetencionDos = Column(Numeric(18, 6))
    idVendedor = Column(Integer)
    TicketCobrado = Column(Integer)
    DescImpLocalTrasladado = Column(String(100))
    usoCFDi = Column(String(4))
    TipoRelacion = Column(String(2))
    TipoComprobante = Column(String(1))
    RFC_PAC = Column(String(13))
    ObservacionesReceta = Column(String(500))
    idProcesoTempladora = Column(Integer)
    idFacturaDividida = Column(Integer)
    esFacturaGlobal = Column(Integer)
    FechaVencimientoCredito = Column(DateTime)
    idObra = Column(Integer)
    idUsuarioCancela = Column(Integer)
    AutoFactura = Column(Integer)
    FolioAutoFactura = Column(String(50))
    idDevolucion = Column(Integer)
    ClaveCancelacion = Column(String(2))
    FolioSustituye = Column(String(50))
    Exportacion = Column(String(2))
    GlobalPeriodicidad = Column(String(2))
    GlobalMeses = Column(String(2))
    GlobalAnno = Column(String(4))
    CodIdentifForestal = Column(String(20))
    OficioAutorizacion = Column(String(20))
    RFN = Column(String(20))
    app = Column(Integer)
    idAlmacen = Column(Integer)
    UtilizadoNotaCredito = Column(Numeric(18, 6))
    idFacturaRelacionada = Column(Integer)

class RegimenFiscal(Base):
    __tablename__ = 'RegimenFiscal'
    idRegimenFiscal = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveRegimenFiscal = Column(String(3), nullable=False)
    RegimenFiscal = Column(String(300), nullable=False)

class CartaPorte_c_RegimenAduanero(Base):
    __tablename__ = 'CartaPorte_c_RegimenAduanero'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveRegimenAduanero = Column(String(3), nullable=False)
    DescripcionRegimenAduanero = Column(String(500))

class TransferenciasTempTallasIVD(Base):
    __tablename__ = 'TransferenciasTempTallasIVD'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idTransferenciaTempTallas = Column(Integer, nullable=False)
    idOrigen = Column(Integer, nullable=False)
    idDestino = Column(Integer, nullable=False)
    idTalla = Column(Integer, nullable=False)
    idColor = Column(Integer, nullable=False)
    CodigoBarras = Column(String(50), nullable=False)
    Cantidad = Column(Integer, nullable=False)
    Surtido = Column(Integer, nullable=False)
    SurtidoTemp = Column(Integer, nullable=False)
    idProductoOrigen = Column(Integer)
    idProductoDestino = Column(Integer)

class FacturasComplementoCartaPorteMercanciaGuiasIdentificacion(Base):
    __tablename__ = 'FacturasComplementoCartaPorteMercanciaGuiasIdentificacion'
    idComplementoCartaPorteMercanciaGuiasIdentificacion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorteMercancia = Column(Integer, nullable=False)
    NumeroGuiaIdentificacion = Column(String(30))
    DescripGuiaIdentificacion = Column(String(1000))
    PesoGuiaIdentificacion = Column(Numeric(18, 3))

class ObraDocumentos(Base):
    __tablename__ = 'ObraDocumentos'
    idObraDocumento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idObra = Column(Integer, nullable=False)
    Descripcion = Column(String(500), nullable=False)
    RutaDocumento = Column(String(1000), nullable=False)
    idObraTipoDocumento = Column(Integer)
    idRevisado = Column(SmallInteger)
    idObraTipoOtroDocumento = Column(Integer)
    Ruta = Column(String(1000))

class NOMINA_DetalleEmpleados(Base):
    __tablename__ = 'NOMINA_DetalleEmpleados'
    idNominaDetalleEmpleados = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idNomina = Column(Integer, nullable=False)
    idEmpleado = Column(Integer, nullable=False)

class ComisionistaObservaciones(Base):
    __tablename__ = 'ComisionistaObservaciones'
    idComisionistaObservaciones = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComisionista = Column(Integer, nullable=False)
    Observaciones = Column(String(250), nullable=False)
    Fecha = Column(DateTime, nullable=False)
    idUsuario = Column(Integer, nullable=False)

class Empresa(Base):
    __tablename__ = 'Empresa'
    idEmpresa = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Nombre = Column(String(300))
    Alias = Column(String(300))
    Logo = Column(String(300))
    RFC = Column(String(13), nullable=False)
    Calle = Column(String(150))
    NumeroExterior = Column(String(50))
    NumeroInterior = Column(String(50))
    Colonia = Column(String(100))
    Localidad = Column(String(100))
    Referencia = Column(String(100))
    Municipio = Column(String(100))
    Estado = Column(String(100))
    Pais = Column(String(100))
    CodigoPostal = Column(String(5), nullable=False)
    RepresentanteLegal = Column(String(100))
    Telefonos = Column(String(100))
    email = Column(String(100))
    PaginaWeb = Column(String(100))
    Logotipo = Column(LargeBinary)
    Leyenda = Column(String(1000))
    Fecha = Column(DateTime)
    esGas = Column(Integer)
    CuentaContablePoliza = Column(String(20))
    NombreCuentaContable = Column(String(255))
    Prefijo = Column(String(10))
    RutaCedula = Column(String(150))
    Cedula = Column(LargeBinary)
    esConst = Column(Integer)
    RutaArchivos = Column(String(250))
    RutaArchivosNomina = Column(String(250))
    RegimenFiscal = Column(String(100), nullable=False)
    Eliminar = Column(Integer)
    esCBB = Column(Integer)
    idPAC = Column(Integer)
    esCervecera = Column(Integer)
    RegistroPatronal = Column(String(20))
    CURP = Column(String(18))
    MensajeProveedor = Column(String(250))
    MensajeFactura = Column(String(250))
    Banco = Column(String(25))
    CuentaBanco = Column(String(25))
    CLABEBanco = Column(String(25))
    MostrarMensajeRespaldo = Column(SmallInteger)
    LeyendaCotizacion = Column(String(1000))
    EsPuntoVenta = Column(Integer)
    ClaveRegimenFiscal = Column(String(3))
    ClaveEstado = Column(String(3))
    ClavePais = Column(String(3))
    esEscuela = Column(Integer)
    idGESEM = Column(VARBINARY)
    esDEMO = Column(VARBINARY)
    RegimenCapital = Column(String(50))
    esAbarrote = Column(Integer)

class TransferenciasTempIVD(Base):
    __tablename__ = 'TransferenciasTempIVD'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idTransferenciaTemp = Column(Integer, nullable=False)
    idOrigen = Column(Integer, nullable=False)
    idDestino = Column(Integer, nullable=False)
    Cantidad = Column(Integer, nullable=False)
    Surtido = Column(Integer, nullable=False)
    SurtidoTemp = Column(Integer, nullable=False)
    TIpo = Column(String(1), nullable=False)
    Serie = Column(String(50), nullable=False)
    idProductoOrigen = Column(Integer)
    idProductoDestino = Column(Integer)

class RestaurantCuenta(Base):
    __tablename__ = 'RestaurantCuenta'
    idCuenta = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idMesa = Column(Integer, nullable=False)
    idMesero = Column(Integer, nullable=False)
    NumeroCuenta = Column(Integer)
    Fecha = Column(DateTime, nullable=False)
    SubTotalSinDescuento = Column(Numeric(18, 6), nullable=False)
    Descuento = Column(Numeric(18, 6), nullable=False)
    Total = Column(Numeric(18, 6), nullable=False)
    Observaciones = Column(String(500))
    Estatus = Column(String(1))
    idfactura = Column(Integer)
    SubCuenta = Column(Integer)

class Estados(Base):
    __tablename__ = 'Estados'
    idEstado = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClavePais = Column(String(3), nullable=False)
    ClaveEstado = Column(String(3), nullable=False)
    Descripcion = Column(String(100), nullable=False)

class CartaPorte_c_FormaFarmaceutica(Base):
    __tablename__ = 'CartaPorte_c_FormaFarmaceutica'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveFormaFarmaceutica = Column(String(2), nullable=False)
    DescripcionFormaFarmaceutica = Column(String(500))

class TransferenciasAplicadas(Base):
    __tablename__ = 'TransferenciasAplicadas'
    idTransferenciaAplicada = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idTransferencia = Column(Integer, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    Estatus = Column(String(1), nullable=False)
    idUsuario = Column(Integer, nullable=False)
    fecha = Column(DateTime)

class Obras(Base):
    __tablename__ = 'Obras'
    idObra = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    Descripcion = Column(String(50), nullable=False)
    FechaInicioContrato = Column(DateTime, nullable=False)
    FechaFinContrato = Column(DateTime)
    Calle = Column(String(100))
    NumeroExterior = Column(String(50))
    NumeroInterior = Column(String(50))
    Colonia = Column(String(100))
    Localidad = Column(String(100))
    Municipio = Column(String(100))
    CodigoPostal = Column(String(10))
    Estado = Column(String(100))
    Pais = Column(String(100))
    Lugar = Column(String(500))
    LugarDos = Column(String(500))
    idTipoObra = Column(Integer, nullable=False)
    Presupuesto = Column(Numeric(18, 2), nullable=False)
    idEmpleadoResponsable = Column(Integer, nullable=False)
    idCliente = Column(Integer, nullable=False)
    Estatus = Column(String(1), nullable=False)
    FechaInicioReal = Column(DateTime)
    FechaFinReal = Column(DateTime)
    Observaciones = Column(String(500))
    SubTotal = Column(Numeric(18, 2))
    CincoAlMillar = Column(Numeric(18, 2))
    Amortizacion = Column(Numeric(18, 2))
    IVA = Column(Numeric(18, 2))
    Total = Column(Numeric(18, 2))
    idPresupuesto = Column(Integer)
    NumeroContrato = Column(String(50))
    idProducto = Column(Integer)
    Anno = Column(String(4))

class ProductoBloqueado(Base):
    __tablename__ = 'ProductoBloqueado'
    idProductoBloqueado = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer, nullable=False)
    idPedidoCliente = Column(Integer)
    Cantidad = Column(Numeric(18, 4), nullable=False)
    FechaFinal = Column(DateTime, nullable=False)
    Activo = Column(Integer, nullable=False)
    idFacturaDetalle = Column(Integer)
    idTransferenciaRequisicion = Column(Integer)
    app = Column(Integer)

class ClienteHuellaDigital(Base):
    __tablename__ = 'ClienteHuellaDigital'
    idHuellaDigitalCliente = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCliente = Column(Integer, nullable=False)
    IndiceDerecho = Column(VARBINARY)

class CartaPorte_c_DocumentoAduanero(Base):
    __tablename__ = 'CartaPorte_c_DocumentoAduanero'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveDocumentoAduanero = Column(String(2), nullable=False)
    DescripcionDocumentoAduanero = Column(String(500))

class FacturaMasiva(Base):
    __tablename__ = 'FacturaMasiva'
    idFacturaMasiva = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idPlantillaFactura = Column(Integer)
    idTipoDocumento = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    Nombre = Column(String(50), nullable=False)

class NOMINA(Base):
    __tablename__ = 'NOMINA'
    idNomina = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    Descripcion = Column(String(50), nullable=False)
    FechaInicialPago = Column(DateTime, nullable=False)
    FechaFinalPago = Column(DateTime, nullable=False)
    NumDiasPagados = Column(Numeric(18, 2), nullable=False)
    FechaPago = Column(DateTime, nullable=False)
    idFormaPago = Column(Integer)
    idMetodoPago = Column(String(50))
    idTipoNomina = Column(String(1))
    idPeriodicidadPago = Column(Integer)
    idOrigenRecurso = Column(String(2))
    MontoRecursoPropio = Column(Numeric(18, 4))

class TipoPoliza(Base):
    __tablename__ = 'TipoPoliza'
    idTipoPoliza = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    TipoPoliza = Column(String(50), nullable=False)

class RestaurantCuentaDetalle(Base):
    __tablename__ = 'RestaurantCuentaDetalle'
    idCuentaDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCuenta = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Cantidad = Column(Numeric(18, 4), nullable=False)
    Precio = Column(Numeric(18, 6), nullable=False)
    SubTotalDetalleSinDescuento = Column(Numeric(18, 6), nullable=False)
    PorcientoDescuentoDetalle = Column(Numeric(18, 6), nullable=False)
    DescuentoDetalle = Column(Numeric(18, 6), nullable=False)
    TotalDetalle = Column(Numeric(18, 6), nullable=False)
    Observaciones = Column(String(1000))
    Producto = Column(String(1000))
    esComplementoDe = Column(Integer)
    esModificadorDe = Column(Integer)
    FactorExistencia = Column(Numeric(18, 6))

class PagosComisiones2(Base):
    __tablename__ = 'PagosComisiones2'
    idPagoComision = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFacturaComision = Column(Integer, nullable=False)
    idTipoOperacion = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    Cantidad = Column(Numeric(18, 2), nullable=False)
    NumeroDocumento = Column(String(50))
    idUsuario = Column(Integer)
    idBanco = Column(Integer)
    idCuentaBanco = Column(Integer)
    RutaComprobante = Column(String(1000))

class CartaPorte_c_CondicionesEspTransp(Base):
    __tablename__ = 'CartaPorte_c_CondicionesEspTransp'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveCondicionesEspTransp = Column(String(2), nullable=False)
    DescripcionCondicionesEspTransp = Column(String(500))

class FacturaMasivaDetalle(Base):
    __tablename__ = 'FacturaMasivaDetalle'
    idFacturaMasivaDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFacturaMasiva = Column(Integer, nullable=False)
    idCliente = Column(Integer, nullable=False)
    Codigo = Column(String(20), nullable=False)
    RFC = Column(String(13), nullable=False)
    Nombre = Column(String(300), nullable=False)
    idFactura = Column(Integer)
    Folio = Column(Integer)
    UUID = Column(String(50))
    RutaXML = Column(String(500))
    Serie = Column(String(50))
    Importe = Column(Numeric(18, 2))

class TipoGastoDetalle(Base):
    __tablename__ = 'TipoGastoDetalle'
    idTipoGastoDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idTipoGasto = Column(Integer, nullable=False)
    TipoGastoDetalle = Column(String(50), nullable=False)

class ObraTipoOtroDocumento(Base):
    __tablename__ = 'ObraTipoOtroDocumento'
    idObraTipoOtroDocumento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ObraTipoOtroDocumento = Column(String(50), nullable=False)

class NOMINA_Banco(Base):
    __tablename__ = 'NOMINA_Banco'
    idBanco = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveBanco = Column(String(3), nullable=False)
    Banco = Column(String(100), nullable=False)

class CartaPorte_c_CodigoPostal(Base):
    __tablename__ = 'CartaPorte_c_CodigoPostal'
    id = Column(Integer, primary_key=True, autoincrement=True)
    CodigoPostal = Column(String(10), nullable=False)
    ClaveEstado = Column(String(3), nullable=False)
    ClaveMunicipio = Column(String(3))
    ClaveLocalidad = Column(String(2))

class ViaticoComprobacion(Base):
    __tablename__ = 'ViaticoComprobacion'
    idViaticoComprobacion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idViatico = Column(Integer, nullable=False)
    idTipoViatico = Column(Integer, nullable=False)
    idObra = Column(Integer, nullable=False)
    NumeroDocumento = Column(String(50), nullable=False)
    FechaComprobacion = Column(DateTime, nullable=False)
    Importe = Column(Numeric(18, 2), nullable=False)
    Observaciones = Column(String(200))

class NOMINA_TipoOtroPago(Base):
    __tablename__ = 'NOMINA_TipoOtroPago'
    idTipoOtroPago = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveTipoOtroPago = Column(String(3), nullable=False)
    TipoOtroPago = Column(String(150), nullable=False)

class SurtirFactura(Base):
    __tablename__ = 'SurtirFactura'
    idSurtirFactura = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer)
    idCompra = Column(Integer)
    idProducto = Column(Integer, nullable=False)
    Cantidad = Column(Numeric(18, 6), nullable=False)
    Fecha = Column(DateTime)
    idUsuario = Column(Integer, nullable=False)
    Tipo = Column(String(40), nullable=False)

class TMP_EtiquetasCompras(Base):
    __tablename__ = 'TMP_EtiquetasCompras'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idCompra = Column(Integer)
    idProducto = Column(Integer)
    Identificador = Column(String(50))
    Producto = Column(String(1000))
    Proveedor = Column(String(20))
    Fecha = Column(DateTime)
    CodigoBarras = Column(LargeBinary)
    Alias = Column(String(300))
    precioventaenclave = Column(String(10))
    PrecioVenta = Column(Numeric(18, 2))
    Moneda = Column(String(10))

class ProductoSimilar(Base):
    __tablename__ = 'ProductoSimilar'
    idProductoSimilar = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer, nullable=False)
    idProductoSimilarHijo = Column(Integer, nullable=False)

class SARIMA_Proyeccion(Base):
    __tablename__ = 'SARIMA_Proyeccion'
    idProyeccion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    fecha = Column(DateTime)
    identificador = Column(String(50))
    producto = Column(String(500))
    existencias = Column(String(5))
    tiempoEntrega = Column(String(5))
    ciclo = Column(String(6))
    pronosticoCiclo = Column(String(20))
    ajusteCiclo = Column(String(6))
    pedirSinBackOrder = Column(String(6))
    backOrderUno = Column(String(6))
    fechaBackOrderUno = Column(String(10))
    backOrderDos = Column(String(6))
    fechaBackOrderDos = Column(String(10))
    Observaciones = Column(String(500))

class NOMINA_MovimientosOtroPago(Base):
    __tablename__ = 'NOMINA_MovimientosOtroPago'
    idNominaOtroPago = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idNominaMovimiento = Column(Integer, nullable=False)
    TipoOtroPago = Column(String(3), nullable=False)
    ClaveOtroPago = Column(String(15), nullable=False)
    ConceptoOtroPago = Column(String(100), nullable=False)
    ImporteOtroPago = Column(Numeric(18, 6), nullable=False)
    SubsidioCausado = Column(Numeric(18, 6))
    SaldoAFavor = Column(Numeric(18, 6))
    Anno = Column(Integer)
    RemanenteSalFav = Column(Numeric(18, 6))

class CartaPorte_c_TipoDeTrafico(Base):
    __tablename__ = 'CartaPorte_c_TipoDeTrafico'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveTipoDeTrafico = Column(String(5), nullable=False)
    DescripcionDeTrafico = Column(String(500))

class FacturasNotaria_DatosProvision(Base):
    __tablename__ = 'FacturasNotaria_DatosProvision'
    idDatosProvision = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    Derecho_Reg_Pub_Propiedad = Column(Numeric(18, 6))
    Avaluos_Gastos = Column(Numeric(18, 6))
    Impuesto_Traslado_Dominio = Column(Numeric(18, 6))
    ISR = Column(Numeric(18, 6))
    IVA = Column(Numeric(18, 6))
    Total = Column(Numeric(18, 6))

class NombrePestanaPuntoventa(Base):
    __tablename__ = 'NombrePestanaPuntoventa'
    idNombrePestanaPuntoventa = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    NombrePestanaPuntoventa = Column(String(15), nullable=False)

class EmpresaMail(Base):
    __tablename__ = 'EmpresaMail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idEmpresa = Column(Integer, nullable=False)
    DireccionCorreo = Column(String(100), nullable=False)
    SMTPHost = Column(String(50), nullable=False)
    SMTPPort = Column(Integer, nullable=False)
    HabilitarSSL = Column(Integer, nullable=False)
    Usuario = Column(String(50), nullable=False)
    Contrasena = Column(String(50), nullable=False)
    Mensaje = Column(String(500))

class SARIMA_Parametros(Base):
    __tablename__ = 'SARIMA_Parametros'
    idParametro = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Nombre = Column(String(20))
    ValorInferior = Column(Numeric(18, 4))
    ValorSuperior = Column(Numeric(18, 4))
    idEmpresa = Column(Integer)

class ObraPresupuesto(Base):
    __tablename__ = 'ObraPresupuesto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idObra = Column(Integer)
    FechaPresupuesto = Column(DateTime)
    Presupuesto = Column(Numeric(18, 2))

class ProductoCodigo(Base):
    __tablename__ = 'ProductoCodigo'
    idProductoCodigo = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer, nullable=False)
    idPrecio = Column(Integer)
    CantidadIncluida = Column(Numeric(18, 4))
    CodigoDeBarras = Column(String(50))
    NombrePrecio = Column(String(50))

class FacturasDetalle(Base):
    __tablename__ = 'FacturasDetalle'
    idFacturaDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Cantidad = Column(Numeric(18, 6), nullable=False)
    PrecioInicial = Column(Numeric(18, 6), nullable=False)
    PrecioFinal = Column(Numeric(18, 6), nullable=False)
    SubTotalSinDescuentoDetalle = Column(Numeric(18, 6))
    PorcentajeDescuento = Column(Numeric(18, 10), nullable=False)
    SubTotalConDescuentoDetalle = Column(Numeric(18, 6))
    ImporteIVA = Column(Numeric(18, 6), nullable=False)
    IEPS = Column(Numeric(18, 6))
    RetIVA = Column(Numeric(18, 6))
    ISR = Column(Numeric(18, 6))
    IMCD = Column(Numeric(18, 6))
    ISSH = Column(Numeric(18, 6))
    TotalDetalle = Column(Numeric(18, 6))
    Observaciones = Column(String(1000))
    nombreAlumno = Column(String(150))
    CURP = Column(String(18))
    nivelEducativo = Column(String(40))
    autRVOE = Column(String(10))
    ComplementoAduana = Column(String(100))
    ComplementoFechaPedimento = Column(String(100))
    ComplementoPedimento = Column(String(1000))
    Devuelto = Column(Numeric(18, 6))
    CuentaPredial = Column(String(100))
    ExistenciaFinal = Column(Numeric(18, 4))
    idProductoSeries = Column(String(500))
    PorcientoIEPS = Column(Numeric(18, 6))
    idProductoLotes = Column(String(500))
    DescImpLocalTrasladado = Column(String(100))
    Tara = Column(Numeric(18, 4))
    PorcientoIVA = Column(Numeric(18, 6))
    PorcientoRetIVA = Column(Numeric(18, 6))
    PorcientoISR = Column(Numeric(18, 6))
    Exento = Column(Integer)
    idProductoTallas = Column(String(500))
    esPaquete = Column(Integer)
    DescuentoDetalle = Column(Numeric(18, 6))
    IdentificadorProducto = Column(String(50))
    FechaInicialContrato = Column(DateTime)
    FechaFinalContrato = Column(DateTime)
    FactorExistencia = Column(Numeric(18, 6))
    DescripcionProducto = Column(String(1000))
    idMotivoDescuento = Column(Integer)
    Placas = Column(String(50))
    FolioHolograma = Column(BigInteger)
    PrecioCompra = Column(Numeric(18, 6))
    PorcentajeDescuento1 = Column(Numeric(18, 10))
    DescuentoDetalle1 = Column(Numeric(18, 6))
    RfcACuentaTerceros = Column(String(20))
    NombreACuentaTerceros = Column(String(254))
    RegimenFiscalACuentaTerceros = Column(String(3))
    DomicilioFiscalACuentaTerceros = Column(String(6))
    idFacturaDevolucion = Column(Integer)
    AnualidadContrato = Column(Numeric(18, 6))
    idPedidoCliente = Column(Integer)
    Surtido = Column(Numeric(18, 6))

class CondicionesPago(Base):
    __tablename__ = 'CondicionesPago'
    idCondicionesPago = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    CondicionesPago = Column(String(100), nullable=False)

class ProductoHistoricoPrecio(Base):
    __tablename__ = 'ProductoHistoricoPrecio'
    idProductoHistoricoPrecio = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    PrecioAnterior = Column(Numeric(18, 6), nullable=False)
    PrecioNuevo = Column(Numeric(18, 6), nullable=False)
    idUsuario = Column(Integer, nullable=False)
    esVenta = Column(Integer)
    esCompra = Column(Integer)
    esMayoreo = Column(Integer)

class SARIMA_Datos(Base):
    __tablename__ = 'SARIMA_Datos'
    idHistorico = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    identificador = Column(String(50))
    cantidad = Column(Numeric(18, 6))
    idFactura = Column(Integer)
    fecha = Column(DateTime)

class ObraMateriales(Base):
    __tablename__ = 'ObraMateriales'
    idObraMateriales = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idObra = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    NumeroDocumento = Column(String(50), nullable=False)
    Cantidad = Column(Numeric(18, 6), nullable=False)
    Devuelto = Column(Numeric(18, 6), nullable=False)
    Precio = Column(Numeric(18, 6), nullable=False)
    Importe = Column(Numeric(18, 2), nullable=False)
    Observaciones = Column(String(200))

class FarmaciaPresentaciones(Base):
    __tablename__ = 'FarmaciaPresentaciones'
    idPresentacion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Presentacion = Column(String(50), nullable=False)

class ProductoPresentacion(Base):
    __tablename__ = 'ProductoPresentacion'
    idProductoPresentacion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Descripcion = Column(String(50))
    PrecioSinImpuestos = Column(Numeric(18, 6))
    PrecioConImpuestos = Column(Numeric(18, 6))
    FactorExistencia = Column(Numeric(20, 15), nullable=False)
    idUnidadMedida = Column(Integer)
    CodigoDeBarras = Column(String(50))
    CantidadUnidadesIncluidas = Column(Numeric(18, 6))
    idProductoHijo = Column(Integer)

class CartaPorte_c_Ubicacion(Base):
    __tablename__ = 'CartaPorte_c_Ubicacion'
    idUbicacion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    TipoCatalogoUbicacion = Column(String(10))
    IDCatalogoUbicacion = Column(String(8))
    RFCRemitenteDestinatarioCatalogoUbicacion = Column(String(15))
    NombreRemitenteDestinatarioCatalogoUbicacion = Column(String(254))
    NumRegIdTribCatalogoUbicacion = Column(String(40))
    ResidenciaFiscalCatalogoUbicacion = Column(String(5))
    NumEstacionCatalogoUbicacion = Column(String(10))
    NombreEstacionCatalogoUbicacion = Column(String(50))
    NavegacionTraficoCatalogoUbicacion = Column(String(10))
    TipoEstacionCatalogoUbicacion = Column(String(2))
    CalleCatalogoUbicacion = Column(String(100))
    NumeroExteriorCatalogoUbicacion = Column(String(50))
    NumeroInteriorCatalogoUbicacion = Column(String(50))
    ColoniaCatalogoUbicacion = Column(String(120))
    LocalidadCatalogoUbicacion = Column(String(120))
    ReferenciaCatalogoUbicacion = Column(String(250))
    MunicipioCatalogoUbicacion = Column(String(120))
    EstadoCatalogoUbicacion = Column(String(30))
    PaisCatalogoUbicacion = Column(String(5))
    CodigoPostalCatalogoUbicacion = Column(String(12))

class RET_ComplementoIntereses(Base):
    __tablename__ = 'RET_ComplementoIntereses'
    idRetComplemento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCFDIRetencion = Column(Integer, nullable=False)
    SistFinanciero = Column(String(2))
    RetiroAORESRetInt = Column(String(2))
    OperFinancDerivad = Column(String(2))
    MontIntNominal = Column(Numeric(18, 6))
    MontIntReal = Column(Numeric(18, 6))
    Perdida = Column(Numeric(18, 6))

class CartaPorte_c_TipoFiguraParteTransporte(Base):
    __tablename__ = 'CartaPorte_c_TipoFiguraParteTransporte'
    idTipoFiguraParteTransporte = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ParteTransporte = Column(String(10), nullable=False)
    Calle = Column(String(150))
    NumeroExterior = Column(String(50))
    NumeroInterior = Column(String(50))
    Colonia = Column(String(100))
    Localidad = Column(String(100))
    Referencia = Column(String(100))
    Municipio = Column(String(100))
    Estado = Column(String(100))
    Pais = Column(String(100))
    CodigoPostal = Column(String(6))

class FacturasComplementoPagoEspecies(Base):
    __tablename__ = 'FacturasComplementoPagoEspecies'
    idComplementoPagoEspecies = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    CvePIC = Column(String(25), nullable=False)
    FolioSolDon = Column(String(11), nullable=False)
    PzaArtNombre = Column(String(500), nullable=False)
    PzaArtTecn = Column(String(500), nullable=False)
    PzaArtAProd = Column(String(4), nullable=False)
    PzaArtDim = Column(String(500), nullable=False)

class TransferenciasAplicadasDetalle(Base):
    __tablename__ = 'TransferenciasAplicadasDetalle'
    idTransferenciaAplicadaDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idTransferenciaAplicada = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Cantidad = Column(Numeric(18, 6), nullable=False)
    Series = Column(Integer, nullable=False)
    Tallas = Column(Integer, nullable=False)
    Lotes = Column(Integer, nullable=False)

class Cotizaciones(Base):
    __tablename__ = 'Cotizaciones'
    idCotizacion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idCliente = Column(Integer, nullable=False)
    NombreCliente = Column(String(150))
    NumeroCotizacion = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    PorcentajeDescuento = Column(Numeric(18, 4), nullable=False)
    SubTotalAntesDescuento = Column(Numeric(18, 6), nullable=False)
    ImporteDescuento = Column(Numeric(18, 6), nullable=False)
    ImporteIVA = Column(Numeric(18, 6))
    Total = Column(Numeric(18, 6))
    Observaciones = Column(String(500))
    idFactura = Column(Integer)
    idUsuario = Column(Integer)
    RutaPDF = Column(String(500))
    CantidadLetra = Column(String(250))
    Costo = Column(Numeric(18, 6))
    ImprimirModelo = Column(Integer)
    ImprimirClave = Column(Integer)
    idMoneda = Column(Integer)
    ImporteIEPS = Column(Numeric(18, 6))
    idVendedor = Column(Integer)
    FolioInternoPresupuesto = Column(String(40))
    DirectorioObra = Column(String(1000))
    idProceso = Column(Integer)
    idCanal = Column(Integer)
    GD_web = Column(Integer)
    ImporteRetIVA = Column(Numeric(18, 6))
    ImporteISR = Column(Numeric(18, 6))

class Cobros(Base):
    __tablename__ = 'Cobros'
    idCobro = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    idTipoOperacion = Column(Integer)
    idBanco = Column(Integer)
    Fecha = Column(DateTime, nullable=False)
    Cantidad = Column(Numeric(18, 2), nullable=False)
    NumeroDocumento = Column(String(50))
    idUsuario = Column(Integer)
    Observaciones = Column(String(100))
    idBancoOrigen = Column(Integer)
    FechaCaptura = Column(DateTime)
    idCuentaBanco = Column(Integer)
    idNotaVenta = Column(Integer)
    FoliosFacturas = Column(String(100))
    RutaComprobante = Column(String(1000))
    Verificado = Column(Boolean)
    idFormaPago = Column(String(10))
    idComplementoPago = Column(Integer)
    idCobrador = Column(Integer)
    app = Column(Integer)
    RecibidoUSD = Column(Numeric(18, 2))
    TipoCambio = Column(Numeric(18, 2))
    idNotadeCredito = Column(Integer)
    esDevolucion = Column(Boolean)

class ConteoFisico(Base):
    __tablename__ = 'ConteoFisico'
    idConteoFisico = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    NombreArchivo = Column(String(150), nullable=False)
    idUsuario = Column(Integer, nullable=False)

class TransferenciasAlmacenesIVD(Base):
    __tablename__ = 'TransferenciasAlmacenesIVD'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idTransferenciaAlmacen = Column(Integer, nullable=False)
    idProductoOrigen = Column(Integer, nullable=False)
    idProductoDestino = Column(Integer, nullable=False)
    Cantidad = Column(Integer, nullable=False)
    Surtido = Column(Integer, nullable=False)
    SurtidoTemp = Column(Integer, nullable=False)

class EmpresaFolios(Base):
    __tablename__ = 'EmpresaFolios'
    idEmpresaFolio = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idTipoDocumento = Column(Integer, nullable=False)
    Serie = Column(String(10))
    FolioInicial = Column(Integer, nullable=False)
    Estatus = Column(String(1))
    UltimoFolioUsado = Column(Integer, nullable=False)
    idUsuarioUtiliza = Column(Integer)
    idAlmacen = Column(Integer)

class FacturasComplementoDonatarias(Base):
    __tablename__ = 'FacturasComplementoDonatarias'
    idComplementoDonatarias = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    NumeroAutorizacion = Column(String(50), nullable=False)
    fechaAutorizacion = Column(DateTime, nullable=False)
    leyenda = Column(String(1000), nullable=False)

class FormaPago(Base):
    __tablename__ = 'FormaPago'
    idFormaPago = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    FormaPago = Column(String(100), nullable=False)

class RestaurantZonasImpresion(Base):
    __tablename__ = 'RestaurantZonasImpresion'
    idZonaImpresion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Nombre = Column(String(100), nullable=False)
    Ruta = Column(String(100), nullable=False)

class ObraDevolucion(Base):
    __tablename__ = 'ObraDevolucion'
    idObraDevolucion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idObraMateriales = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    Cantidad = Column(Numeric(18, 6), nullable=False)
    Observaciones = Column(String(200))

class SerieConsecutivo(Base):
    __tablename__ = 'SerieConsecutivo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    consecutivo = Column(Integer, nullable=False)
    anhoNuevoReiniciar = Column(Integer)

class NOMINA_MovimientosSubcontratacion(Base):
    __tablename__ = 'NOMINA_MovimientosSubcontratacion'
    idSubcontratacion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idNominaMovimiento = Column(Integer, nullable=False)
    RFCLabora = Column(String(13), nullable=False)
    PorcentajeTiempo = Column(Integer, nullable=False)

class RET_CFDiRelacionados(Base):
    __tablename__ = 'RET_CFDiRelacionados'
    idCFDiRelacionado = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCFDIRetencion = Column(Integer, nullable=False)
    idCFDIRetencionRelacionada = Column(Integer)
    Folio = Column(String(50), nullable=False)
    TipoRelacion = Column(String(2))
    UUID = Column(String(50), nullable=False)

class CartaPorte_c_Autotransporte(Base):
    __tablename__ = 'CartaPorte_c_Autotransporte'
    idAutoTransporte = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    PermSCT = Column(String(10), nullable=False)
    NumPermisoSCT = Column(String(50), nullable=False)
    ConfigVehicular = Column(String(10), nullable=False)
    PlacaVM = Column(String(10), nullable=False)
    AnioModeloVM = Column(String(4), nullable=False)
    SubTipoRem1 = Column(String(7))
    PlacaRemolque1 = Column(String(10))
    SubTipoRem2 = Column(String(7))
    PlacaRemolque2 = Column(String(10))
    AseguraRespCivil = Column(String(50))
    PolizaRespCivil = Column(String(30))
    AseguraMedAmbiente = Column(String(50))
    PolizaMedAmbiente = Column(String(30))
    AseguraCarga = Column(String(50))
    PolizaCarga = Column(String(30))
    PrimaSeguro = Column(Numeric(18, 2))
    PesoBrutoVehicular = Column(Numeric(18, 2))

class RestaurantImprimirAPP(Base):
    __tablename__ = 'RestaurantImprimirAPP'
    idRestaurantImprimir = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComanda = Column(Integer, nullable=False)
    Imprimir = Column(Integer, nullable=False)

class TransportistaUnidades(Base):
    __tablename__ = 'TransportistaUnidades'
    idTransporteUnidad = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Unidad = Column(String(100), nullable=False)
    Marca = Column(String(50), nullable=False)
    Placa = Column(String(20), nullable=False)
    Observaciones = Column(String(500), nullable=False)
    idTransporteOperador = Column(Integer, nullable=False)
    Estatus = Column(String(1), nullable=False)

class UsuariosHuellaDigital(Base):
    __tablename__ = 'UsuariosHuellaDigital'
    idHuellaDigitalUsuario = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idUsuario = Column(Integer, nullable=False)
    IndiceDerecho = Column(VARBINARY)

class FacturasComplementoCartaPorteMercancia(Base):
    __tablename__ = 'FacturasComplementoCartaPorteMercancia'
    idComplementoCartaPorteMercancia = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorteMercancias = Column(Integer, nullable=False)
    BienesTransp = Column(String(8))
    ClaveSTCC = Column(String(10))
    Descripcion = Column(String(1000))
    Cantidad = Column(Numeric(18, 6))
    ClaveUnidad = Column(String(10))
    Unidad = Column(String(20))
    Dimensiones = Column(String(50))
    MaterialPeligroso = Column(String(2))
    CveMaterialPeligroso = Column(String(10))
    Embalaje = Column(String(10))
    DescripEmbalaje = Column(String(100))
    PesoEnKg = Column(Numeric(18, 3))
    ValorMercancia = Column(Numeric(18, 2))
    Moneda = Column(String(5))
    FraccionArancelaria = Column(String(50))
    UUIDComercioExt = Column(String(50))
    SectorCOFEPRIS = Column(String(2))
    NombreIngredienteActivo = Column(String(1000))
    NomQuimico = Column(String(150))
    DenominacionGenericaProd = Column(String(50))
    DenominacionDistintivaProd = Column(String(50))
    Fabricante = Column(String(240))
    FechaCaducidad = Column(DateTime)
    LoteMedicamento = Column(String(10))
    FormaFarmaceutica = Column(String(2))
    CondicionesEspTransp = Column(String(2))
    RegistroSanitarioFolioAutorizacion = Column(String(15))
    PermisoImportacion = Column(String(6))
    FolioImpoVUCEM = Column(String(25))
    NumCAS = Column(String(15))
    RazonSocialEmpImp = Column(String(80))
    NumRegSanPlagCOFEPRIS = Column(String(60))
    DatosFabricante = Column(String(600))
    DatosFormulador = Column(String(600))
    DatosMaquilador = Column(String(600))
    UsoAutorizado = Column(String(1000))
    TipoMateria = Column(String(2))
    DescripcionMateria = Column(String(50))

class ObraEmpleado(Base):
    __tablename__ = 'ObraEmpleado'
    idObraEmpleado = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idObra = Column(Integer, nullable=False)
    idEmpleado = Column(Integer, nullable=False)

class TransportistaOperadores(Base):
    __tablename__ = 'TransportistaOperadores'
    idTransporteOperador = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Nombre = Column(String(100), nullable=False)
    FechaIngreso = Column(DateTime, nullable=False)
    Estatus = Column(String(1), nullable=False)

class TipoProducto(Base):
    __tablename__ = 'TipoProducto'
    idTipoProducto = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    Descripcion = Column(String(50), nullable=False)
    ControlInventarios = Column(SmallInteger, nullable=False)
    PorImporte = Column(SmallInteger, nullable=False)
    imagenTipoProducto = Column(LargeBinary)
    idZonaImpresion = Column(Integer)
    Comandero = Column(Integer)
    AutoCotizador = Column(Integer)
    Bascula = Column(Integer)
    EC_eCommerce = Column(SmallInteger)
    CotizadorTouch = Column(Integer)
    PromocionFamilia = Column(String(10))
    Medicamento = Column(Integer)
    MaxPorcientoDescuento = Column(Numeric(18, 4))
    Puntos = Column(Integer)
    PorcentajeComision = Column(Numeric(18, 4))

class FacturasComplementoLeyendasFiscales(Base):
    __tablename__ = 'FacturasComplementoLeyendasFiscales'
    idComplementoLeyendasFiscales = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    DisposicionFiscal = Column(String(200))
    Norma = Column(String(200))
    TextoLeyenda = Column(String(200))

class FacturasComplementoCartaPorte(Base):
    __tablename__ = 'FacturasComplementoCartaPorte'
    idComplementoCartaPorte = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    TranspInternac = Column(String(2), nullable=False)
    EntradaSalidaMerc = Column(String(10))
    ViaEntradaSalida = Column(String(2))
    TotalDistRec = Column(Numeric(18, 2))
    PaisOrigenDestino = Column(String(3))
    idCCP = Column(String(36))
    RegimenAduanero = Column(String(3))
    RegistroISTMO = Column(String(2))
    UbicacionPoloOrigen = Column(String(2))
    UbicacionPoloDestino = Column(String(2))
    CodigoQR = Column(LargeBinary)

class ProveedorContacto(Base):
    __tablename__ = 'ProveedorContacto'
    idProveedorContacto = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProveedor = Column(Integer, nullable=False)
    Nombre = Column(String(100))
    Cargo = Column(String(100))
    Telefono = Column(String(100))

class Canal(Base):
    __tablename__ = 'Canal'
    idCanal = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Canal = Column(String(50), nullable=False)

class ObraTipoDocumento(Base):
    __tablename__ = 'ObraTipoDocumento'
    idObraTipoDocumento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ObraTipoDocumento = Column(String(50), nullable=False)

class FacturasComplementoServParcialesConst(Base):
    __tablename__ = 'FacturasComplementoServParcialesConst'
    idComplementoServParcialesConst = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    NumPerLicoAut = Column(String(40), nullable=False)
    Calle = Column(String(150), nullable=False)
    NoExterior = Column(String(55))
    NoInterior = Column(String(30))
    Colonia = Column(String(100))
    Localidad = Column(String(100))
    Referencia = Column(String(100))
    Municipio = Column(String(100), nullable=False)
    Estado = Column(String(2), nullable=False)
    CodigoPostal = Column(String(5), nullable=False)

class ProductoFabricadoPlantilla(Base):
    __tablename__ = 'ProductoFabricadoPlantilla'
    idProductoFabricadoPlantilla = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer, nullable=False)
    idProductoParte = Column(Integer, nullable=False)
    Cantidad = Column(Numeric(14, 4), nullable=False)

class FacturasComplementoCartaPorteMercanciasTranspAereo(Base):
    __tablename__ = 'FacturasComplementoCartaPorteMercanciasTranspAereo'
    idComplementoCartaPorteMercanciasTranspAereo = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorteMercancias = Column(Integer, nullable=False)
    PermSCTAereo = Column(String(10), nullable=False)
    NumPermisoSCTAereo = Column(String(50), nullable=False)
    MatriculaAeronaveAereo = Column(String(11), nullable=False)
    NombreAsegAereo = Column(String(50), nullable=False)
    NumPolizaSeguroAereo = Column(String(30), nullable=False)
    NumeroGuiaAereo = Column(String(15), nullable=False)
    LugarContratoAereo = Column(String(120), nullable=False)
    CodigoTransportistaAereo = Column(String(7))
    RFCEmbarcadorAereo = Column(String(13))
    NumRegIdTribEmbarcAereo = Column(String(40))
    ResidenciaFiscalEmbarcAereo = Column(String(3))
    NombreEmbarcadorAereo = Column(String(254))

class MS_ServicioCliente_Log(Base):
    __tablename__ = 'MS_ServicioCliente_Log'
    idLog = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idServicioCliente = Column(Integer)
    idUsuario = Column(Integer)
    fecha = Column(DateTime)
    accion = Column(String(100))
    valorAnterior = Column(String(1000))
    valorNuevo = Column(String(1000))

class RET_CatalogoRetencion(Base):
    __tablename__ = 'RET_CatalogoRetencion'
    idRetencion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveRetencion = Column(String(2), nullable=False)
    DescripcionRetencion = Column(String(200), nullable=False)

class FacturasComplementoCoordinados(Base):
    __tablename__ = 'FacturasComplementoCoordinados'
    idComplementoCoordinados = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    ClaveVehicular = Column(String(150))
    Placa = Column(String(150))
    RFCPF = Column(String(13))

class SerieFolioPedido(Base):
    __tablename__ = 'SerieFolioPedido'
    idSerieFolioPedido = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Serie = Column(String(25))
    Folio = Column(String(25), nullable=False)
    idUsuario = Column(Integer, nullable=False)

class ClienteContacto(Base):
    __tablename__ = 'ClienteContacto'
    idClienteContacto = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCliente = Column(Integer, nullable=False)
    Nombre = Column(String(100))
    Cargo = Column(String(100))
    Telefono = Column(String(100))

class Productos(Base):
    __tablename__ = 'Productos'
    idProducto = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    Identificador = Column(String(50))
    Producto = Column(String(1000), nullable=False)
    Modelo = Column(String(50))
    Precio = Column(Numeric(14, 6), nullable=False)
    PrecioConIva = Column(Numeric(14, 6))
    PrecioCompra = Column(Numeric(14, 6))
    PrecioMayorista = Column(Numeric(14, 6))
    idTipoProducto = Column(Integer, nullable=False)
    idUnidadMedida = Column(Integer)
    CodigoBarras = Column(LargeBinary)
    Existencia = Column(Numeric(14, 4), nullable=False)
    IEPS = Column(Numeric(14, 6))
    AplicaIVA = Column(SmallInteger, nullable=False)
    Maximo = Column(Numeric(14, 4))
    Minimo = Column(Numeric(14, 4))
    idUsuario = Column(Integer)
    idMoneda = Column(Integer)
    PorcientoUtilidad = Column(Numeric(14, 6))
    Precio3 = Column(Numeric(14, 6))
    Precio4 = Column(Numeric(14, 6))
    Precio5 = Column(Numeric(14, 6))
    idAlmacen = Column(Integer, nullable=False)
    Imagen = Column(LargeBinary)
    FechaAlta = Column(DateTime)
    isRetornable = Column(SmallInteger)
    CantidadBotellas = Column(SmallInteger)
    VentaIndividual = Column(SmallInteger)
    CodigoDeBarras = Column(String(50))
    PorcientoIEPS = Column(Numeric(18, 6))
    Estatus = Column(String(1))
    CodigoProveedor = Column(String(100))
    Lote = Column(String(50))
    Serie = Column(String(50))
    FechaCaducidad = Column(DateTime)
    Producto2 = Column(String(500))
    idTipoProductoDetalle = Column(Integer)
    ClaveProdServ = Column(String(10))
    PorcentajeDescuento = Column(Numeric(18, 4))
    Precio6 = Column(Numeric(14, 6))
    Precio7 = Column(Numeric(14, 6))
    Precio8 = Column(Numeric(14, 6))
    Precio9 = Column(Numeric(14, 6))
    Precio10 = Column(Numeric(14, 6))
    Precio11 = Column(Numeric(14, 6))
    Precio12 = Column(Numeric(14, 6))
    Precio13 = Column(Numeric(14, 6))
    Precio14 = Column(Numeric(14, 6))
    Precio15 = Column(Numeric(14, 6))
    Precio16 = Column(Numeric(14, 6))
    Precio17 = Column(Numeric(14, 6))
    Precio18 = Column(Numeric(14, 6))
    Precio19 = Column(Numeric(14, 6))
    Precio20 = Column(Numeric(14, 6))
    RequiereReceta = Column(SmallInteger)
    TienePredial = Column(SmallInteger)
    Pedimento = Column(String(200))
    PorcentajePrecio2 = Column(Numeric(18, 4))
    PorcentajePrecio3 = Column(Numeric(18, 4))
    PorcentajePrecio4 = Column(Numeric(18, 4))
    PorcentajePrecio5 = Column(Numeric(18, 4))
    PorcentajePrecio6 = Column(Numeric(18, 4))
    PorcentajePrecio7 = Column(Numeric(18, 4))
    PorcentajePrecio8 = Column(Numeric(18, 4))
    PorcentajePrecio9 = Column(Numeric(18, 4))
    PorcentajePrecio10 = Column(Numeric(18, 4))
    PorcentajePrecio11 = Column(Numeric(18, 4))
    PorcentajePrecio12 = Column(Numeric(18, 4))
    PorcentajePrecio13 = Column(Numeric(18, 4))
    PorcentajePrecio14 = Column(Numeric(18, 4))
    PorcentajePrecio15 = Column(Numeric(18, 4))
    PorcentajePrecio16 = Column(Numeric(18, 4))
    PorcentajePrecio17 = Column(Numeric(18, 4))
    PorcentajePrecio18 = Column(Numeric(18, 4))
    PorcentajePrecio19 = Column(Numeric(18, 4))
    PorcentajePrecio20 = Column(Numeric(18, 4))
    Facturable = Column(Integer)
    CostoActual = Column(Numeric(14, 6))
    UnidadConversion = Column(Numeric(14, 6))
    UbicacionDescripcion = Column(String(500))
    UbicacionPasillo = Column(String(50))
    UbicacionFila = Column(String(50))
    UbicacionNivel = Column(String(50))
    PorcentajeComision = Column(Numeric(16, 2))
    ImporteComision = Column(Numeric(16, 2))
    Utilidad = Column(Numeric(16, 2))
    Peso = Column(Numeric(16, 4))
    Puntos = Column(Integer)
    idComplementoSAT = Column(Integer)
    EC_eCommerce = Column(Integer)
    PaqueteVirtual = Column(Integer)
    idPresentacion = Column(Integer)
    imagen2 = Column(LargeBinary)
    imagen3 = Column(LargeBinary)
    imagen4 = Column(LargeBinary)
    imagen5 = Column(LargeBinary)
    app = Column(Integer)
    todosLosClientes = Column(SmallInteger)
    tiempoEntregaProv = Column(Integer)
    ajusteCiclo = Column(Numeric(18, 2))

class FacturasComplementoPagosImpuestosDR(Base):
    __tablename__ = 'FacturasComplementoPagosImpuestosDR'
    idComplementoPagoImpuestoDR = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoPago = Column(Integer, nullable=False)
    idFactura = Column(Integer, nullable=False)
    UUID = Column(String(50))
    baseDR = Column(Numeric(18, 2))
    impuestoDR = Column(String(3))
    tipoFactorDR = Column(String(10))
    tasaCuotaDR = Column(Numeric(18, 6))
    importeDR = Column(Numeric(18, 2))
    tipoImpuestoDR = Column(String(20))

class MS_CatalogoServicios(Base):
    __tablename__ = 'MS_CatalogoServicios'
    idTipoServicio = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    TipoServicio = Column(String(100))
    Estatus = Column(String(1))
    idEmpresa = Column(Integer)
    idUsuario = Column(Integer)
    Fecha = Column(DateTime)

class RET_CatalogoTipoDividendo(Base):
    __tablename__ = 'RET_CatalogoTipoDividendo'
    idTipoDividendo = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveTipoDividendo = Column(String(2), nullable=False)
    DescripcionTipoDividendo = Column(String(100), nullable=False)

class EmpresaTimbresPago(Base):
    __tablename__ = 'EmpresaTimbresPago'
    idEmpresaTimbrePago = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    Comprados = Column(VARBINARY, nullable=False)
    Disponibles = Column(VARBINARY, nullable=False)
    FechaCompra = Column(DateTime, nullable=False)
    Referencia = Column(String(100), nullable=False)
    Vigencia = Column(Integer, nullable=False)
    Aviso = Column(Integer, nullable=False)
    AsignadosPor = Column(String(50))

class EmpleadoObservaciones(Base):
    __tablename__ = 'EmpleadoObservaciones'
    idEmpleadoObservaciones = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpleado = Column(Integer, nullable=False)
    Observaciones = Column(String(250), nullable=False)
    Fecha = Column(DateTime, nullable=False)
    idUsuario = Column(Integer, nullable=False)
    idCategoria = Column(Integer)

class UsuarioMail(Base):
    __tablename__ = 'UsuarioMail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idUsuario = Column(Integer, nullable=False)
    DireccionCorreo = Column(String(100), nullable=False)
    SMTPHost = Column(String(50), nullable=False)
    SMTPPort = Column(Integer, nullable=False)
    HabilitarSSL = Column(Integer, nullable=False)
    Usuario = Column(String(50), nullable=False)
    Contrasena = Column(String(50), nullable=False)
    Mensaje = Column(String(500))

class MS_CatalogoEstatus(Base):
    __tablename__ = 'MS_CatalogoEstatus'
    idEstatus = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Descripcion = Column(String(50))
    Estatus = Column(String(1))
    idUsuario = Column(Integer)
    Fecha = Column(DateTime)
    idEmpresa = Column(Integer)

class MotivoCancelacion(Base):
    __tablename__ = 'MotivoCancelacion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ClaveMotivoCancelacion = Column(String(2), nullable=False)
    MotivoCancelacion = Column(String(100), nullable=False)

class Pacientes(Base):
    __tablename__ = 'Pacientes'
    idPaciente = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    telefono = Column(String(10), nullable=False)
    Nombre = Column(String(100), nullable=False)
    apPaterno = Column(String(100))
    apMaterno = Column(String(100))
    Correo = Column(String(50))
    fechaCreacion = Column(DateTime)
    idEmpresa = Column(Integer, nullable=False)
    FechaNacimiento = Column(String(10))

class CategoriaClienteObservaciones(Base):
    __tablename__ = 'CategoriaClienteObservaciones'
    idCategoriaClienteObservaciones = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Categoria = Column(String(50), nullable=False)
    DescripcionCategoria = Column(String(300), nullable=False)
    Estatus = Column(String(1))

class ProductoDocumentos(Base):
    __tablename__ = 'ProductoDocumentos'
    idProductoDocumento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Descripcion = Column(String(500), nullable=False)
    RutaDocumento = Column(String(-1), nullable=False)

class NombreListaPrecios(Base):
    __tablename__ = 'NombreListaPrecios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Precio1 = Column(String(50), nullable=False)
    Precio2 = Column(String(50), nullable=False)
    Precio3 = Column(String(50), nullable=False)
    Precio4 = Column(String(50), nullable=False)
    Precio5 = Column(String(50), nullable=False)
    Precio6 = Column(String(50), nullable=False)
    Precio7 = Column(String(50), nullable=False)
    Precio8 = Column(String(50), nullable=False)
    Precio9 = Column(String(50), nullable=False)
    Precio10 = Column(String(50), nullable=False)
    Precio11 = Column(String(50), nullable=False)
    Precio12 = Column(String(50), nullable=False)
    Precio13 = Column(String(50), nullable=False)
    Precio14 = Column(String(50), nullable=False)
    Precio15 = Column(String(50), nullable=False)
    Precio16 = Column(String(50), nullable=False)
    Precio17 = Column(String(50), nullable=False)
    Precio18 = Column(String(50), nullable=False)
    Precio19 = Column(String(50), nullable=False)
    Precio20 = Column(String(50), nullable=False)

class NOMINA_MovimientosDeducciones(Base):
    __tablename__ = 'NOMINA_MovimientosDeducciones'
    idNominaDeduccion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idNominaMovimiento = Column(Integer, nullable=False)
    TipoDeduccion = Column(String(3), nullable=False)
    ClaveDeduccion = Column(String(15), nullable=False)
    ConceptoDeduccion = Column(String(100), nullable=False)
    ImporteGravadoDeduccion = Column(Numeric(18, 6), nullable=False)
    ImporteExentoDeduccion = Column(Numeric(18, 6))
    ObservacionesDeduccion = Column(String(150))

class MovimientosBancoDetalle(Base):
    __tablename__ = 'MovimientosBancoDetalle'
    idMovimientoDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idMovimiento = Column(Integer, nullable=False)
    idFactura = Column(Integer, nullable=False)
    TotalFactura = Column(Numeric(18, 2))
    cliente_proveedor = Column(String(500))
    Observacion = Column(String(500))

class RET_CatalogoTipoContribuyente(Base):
    __tablename__ = 'RET_CatalogoTipoContribuyente'
    idTipoContribuyente = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveTipoContribuyente = Column(Integer, nullable=False)
    DescripcionTipoContribuyente = Column(String(100), nullable=False)

class NOMINA_RiesgoPuesto(Base):
    __tablename__ = 'NOMINA_RiesgoPuesto'
    idRiesgoPuesto = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveRiesgoPuesto = Column(String(3), nullable=False)
    RiesgoPuesto = Column(String(50), nullable=False)

class Soporte_CatActividad(Base):
    __tablename__ = 'Soporte_CatActividad'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idActividad = Column(Integer, nullable=False)
    NombreActividad = Column(String(50))

class MovimientosTimbresPago(Base):
    __tablename__ = 'MovimientosTimbresPago'
    idMovimientoTimbrePago = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresaTimbrePago = Column(Integer, nullable=False)
    idFactura = Column(Integer, nullable=False)
    UUID = Column(String(50))
    Estatus = Column(String(1), nullable=False)
    Fecha = Column(DateTime, nullable=False)

class RET_CatalogoPais(Base):
    __tablename__ = 'RET_CatalogoPais'
    idPais = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClavePais = Column(String(2), nullable=False)
    Pais = Column(String(200), nullable=False)

class EmpresaRegistroPatronal(Base):
    __tablename__ = 'EmpresaRegistroPatronal'
    idRegistroPatronal = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    RegistroPatronal = Column(String(20))
    Descripcion = Column(String(50))

class Soporte_RegistroActividades(Base):
    __tablename__ = 'Soporte_RegistroActividades'
    idRegistroActividad = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idUsuario = Column(Integer)
    idActividad = Column(Integer)
    Inicio = Column(DateTime)
    Fin = Column(DateTime)

class MovimientosBanco(Base):
    __tablename__ = 'MovimientosBanco'
    idMovimiento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    Concepto = Column(String(1000), nullable=False)
    Cargo = Column(Numeric(18, 2))
    Abono = Column(Numeric(18, 2))
    Folio = Column(String(50))
    TotalFactura = Column(Numeric(18, 2))
    cliente_proveedor = Column(String(100))
    Validado = Column(Boolean)
    Observacion = Column(String(500))

class UnidadMedida(Base):
    __tablename__ = 'UnidadMedida'
    idUnidadMedida = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    UnidadMedida = Column(String(200), nullable=False)
    ClaveUnidadMedida = Column(String(3))
    Estatus = Column(String(1))

class EmpresaTimbres(Base):
    __tablename__ = 'EmpresaTimbres'
    idEmpresaTimbre = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    Comprados = Column(VARBINARY, nullable=False)
    Disponibles = Column(VARBINARY, nullable=False)
    FechaCompra = Column(DateTime, nullable=False)
    Referencia = Column(String(100), nullable=False)
    Vigencia = Column(Integer, nullable=False)
    Aviso = Column(Integer, nullable=False)
    AsignadosPor = Column(String(50))

class FacturasComplementoCartaPorteMercanciasTranspMaritimoContenedor(Base):
    __tablename__ = 'FacturasComplementoCartaPorteMercanciasTranspMaritimoContenedor'
    idComplementoCartaPorteMercanciasTranspMaritinoContenedor = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorteMercanciasTranspMaritino = Column(Integer, nullable=False)
    MatriculaContenedorMaritimo = Column(String(15), nullable=False)
    TipoContenedorMaritimo = Column(String(5), nullable=False)
    NumPrecintoContenedorMaritimo = Column(String(20))
    IdCCPRelacionado = Column(String(36))
    PlacaVMCCP = Column(String(10))
    FechaCertificacionCCP = Column(DateTime)

class RestauranteAPPS(Base):
    __tablename__ = 'RestauranteAPPS'
    idAPP = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Nombre = Column(String(50), nullable=False)
    Estatus = Column(String(1), nullable=False)
    idListaPrecio = Column(Integer, nullable=False)

class ComisionistaDocumentos(Base):
    __tablename__ = 'ComisionistaDocumentos'
    idComisionistaDocumento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComisionista = Column(Integer, nullable=False)
    idComisionistaTipoDocumento = Column(Integer)
    Descripcion = Column(String(500), nullable=False)
    RutaDocumento = Column(String(1000))
    idRevisado = Column(SmallInteger)
    Ruta = Column(String(1000))

class FacturasComplementoCartaPorteMercanciasTranspMaritimo(Base):
    __tablename__ = 'FacturasComplementoCartaPorteMercanciasTranspMaritimo'
    idComplementoCartaPorteMercanciasTranspMaritino = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorteMercancias = Column(Integer, nullable=False)
    PermSCTMaritimo = Column(String(10))
    NumPermisoSCTMaritimo = Column(String(30))
    NombreAsegMaritimo = Column(String(50))
    NumPolizaSeguroMaritimo = Column(String(30))
    TipoEmbarcacionMaritimo = Column(String(3), nullable=False)
    MatriculaMaritimo = Column(String(30), nullable=False)
    NumeroOMIMaritimo = Column(String(12), nullable=False)
    AnioEmbarcacionMaritimo = Column(String(4))
    NombreEmbarcMaritimo = Column(String(50))
    NacionalidadEmbarcMaritimo = Column(String(3))
    UnidadesDeArqBrutoMaritimo = Column(Numeric(18, 3))
    TipoCargaMaritimo = Column(String(3))
    EsloraMaritimo = Column(Numeric(18, 2))
    MangaMaritimo = Column(Numeric(18, 2))
    CaladoMaritimo = Column(Numeric(18, 2))
    LineaNavieraMaritimo = Column(String(50))
    NombreAgenteNavieroMaritimo = Column(String(100))
    NumAutorizacionNavieroMaritimo = Column(String(20))
    NumViajeMaritimo = Column(String(30))
    NumConocEmbarcMaritimo = Column(String(30))
    PuntalMaritimo = Column(Numeric(18, 2))
    PermisoTempNavegacion = Column(String(19))

class Recetas(Base):
    __tablename__ = 'Recetas'
    idReceta = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idDoctor = Column(Integer, nullable=False)
    idPaciente = Column(Integer, nullable=False)
    PresionArterial = Column(String(20))
    Peso = Column(String(20))
    Temperatura = Column(String(20))
    Talla = Column(String(20))
    Edad = Column(Integer, nullable=False)
    Observaciones = Column(String(-1), nullable=False)
    Fecha = Column(DateTime, nullable=False)
    NumeroReceta = Column(Integer)
    Estatus = Column(String(1), nullable=False)
    NumeroRecetaExterno = Column(String(50))

class FacturasComplementoCartaPorteMercanciaDetalle(Base):
    __tablename__ = 'FacturasComplementoCartaPorteMercanciaDetalle'
    idComplementoCartaPorteMercanciaDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorteMercancia = Column(Integer)
    UnidadPesoMerc = Column(String(10))
    PesoBruto = Column(Numeric(18, 3))
    PesoNeto = Column(Numeric(18, 3))
    PesoTara = Column(Numeric(18, 3))
    NumPiezas = Column(Integer)

class HistoricoXMLCambioPrecio(Base):
    __tablename__ = 'HistoricoXMLCambioPrecio'
    id = Column(Integer, primary_key=True, autoincrement=True)
    NombreXMLCambioPrecios = Column(String(1000))

class RestaurantModificadores(Base):
    __tablename__ = 'RestaurantModificadores'
    idRestaurantModificador = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer, nullable=False)

class OperacionCaja(Base):
    __tablename__ = 'OperacionCaja'
    idOperacionCaja = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    NotaVenta = Column(String(55))
    Operacion = Column(String(50), nullable=False)
    Fecha = Column(DateTime, nullable=False)
    Importe = Column(Numeric(19, 4), nullable=False)
    Multiplicador = Column(Integer, nullable=False)
    idUsuario = Column(Integer, nullable=False)
    idFactura = Column(Integer)
    Recibido = Column(Numeric(19, 4))
    Cambio = Column(Numeric(19, 4))
    idFormaPago = Column(String(10))
    idMetodoPago = Column(String(10))
    idCondicionesPago = Column(Integer)
    CorteZ = Column(Integer)
    Moneda = Column(String(3))
    RecibidoUSD = Column(Numeric(19, 4))
    TipoCambio = Column(Numeric(18, 6))
    idEmpresa = Column(Integer)
    PagoCredito = Column(Integer)
    Estatus = Column(String(1))
    app = Column(Integer)

class MonederoLog(Base):
    __tablename__ = 'MonederoLog'
    idLog = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idConfig = Column(Integer)
    idUsuario = Column(Integer)
    fecha = Column(DateTime)
    accion = Column(String(200))
    valorAnterior = Column(String(200))
    valorNuevo = Column(String(200))

class FacturasComplementoCartaPorteMercanciaCantidad(Base):
    __tablename__ = 'FacturasComplementoCartaPorteMercanciaCantidad'
    idComplementoCartaPorteMercanciaCantidad = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorteMercancia = Column(Integer, nullable=False)
    CantidadTransporta = Column(Numeric(18, 6))
    IDOrigenTransporta = Column(String(10))
    IDDestinoTransporta = Column(String(10))
    CvesTransporte = Column(String(2))

class FormaEnvio(Base):
    __tablename__ = 'FormaEnvio'
    idFormaEnvio = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    FormaEnvio = Column(String(100), nullable=False)

class ComplementosSAT(Base):
    __tablename__ = 'ComplementosSAT'
    idComplementoSAT = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ComplementoSAT = Column(String(50), nullable=False)
    NivelConcepto = Column(Integer, nullable=False)

class FacturasComplementoPagosImpuestosP(Base):
    __tablename__ = 'FacturasComplementoPagosImpuestosP'
    idComplementoPagoImpuestoP = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    idComplementoPago = Column(Integer, nullable=False)
    baseP = Column(Numeric(18, 2))
    impuestoP = Column(String(3))
    tipoFactorP = Column(String(10))
    tasaCuotaP = Column(Numeric(18, 6))
    importeP = Column(Numeric(18, 2))
    tipoImpuestoP = Column(String(20))

class NOMINA_MovimientosHorasExtras(Base):
    __tablename__ = 'NOMINA_MovimientosHorasExtras'
    idNominaHoraExtra = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idNominaMovimiento = Column(Integer, nullable=False)
    Dias = Column(Integer, nullable=False)
    TipoHoras = Column(String(20), nullable=False)
    HorasExtra = Column(Integer, nullable=False)
    ImportePagadoHorasExtra = Column(Numeric(18, 6), nullable=False)

class EC_Usuarios(Base):
    __tablename__ = 'EC_Usuarios'
    idUsuario = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Usuario = Column(String(20))
    Password = Column(String(20))
    Fecha_Alta = Column(DateTime)
    Estatus = Column(String(1))
    Nombre = Column(String(50))
    Apellido_Paterno = Column(String(20))
    Apellido_Materno = Column(String(20))
    Telefono = Column(String(10))
    TipoUsuario = Column(String(1))
    idClienteGesem = Column(Integer)
    usoCFDI = Column(String(3))
    RFC = Column(String(13))

class Bancos(Base):
    __tablename__ = 'Bancos'
    idBanco = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Banco = Column(String(50), nullable=False)

class Cliente(Base):
    __tablename__ = 'Cliente'
    idCliente = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    CodigoCliente = Column(String(20), nullable=False)
    Nombre = Column(String(300))
    RFC = Column(String(13), nullable=False)
    Calle = Column(String(150))
    NumeroExterior = Column(String(50))
    NumeroInterior = Column(String(50))
    Colonia = Column(String(100))
    Localidad = Column(String(100))
    Referencia = Column(String(100))
    Municipio = Column(String(100))
    Estado = Column(String(100))
    Pais = Column(String(100))
    CodigoPostal = Column(String(6))
    Contacto = Column(String(100))
    Telefonos = Column(String(100))
    email = Column(String(1000))
    PaginaWeb = Column(String(100))
    CuentaContable = Column(String(20))
    idUsuario = Column(Integer)
    NumCtaPago = Column(String(60))
    FechaAlta = Column(DateTime)
    CodigoBarras = Column(LargeBinary)
    idPAC = Column(Integer)
    idComisionista = Column(Integer)
    isMayorista = Column(Integer)
    Estatus = Column(String(1))
    DiasCredito = Column(Integer)
    LimiteCredito = Column(Numeric(18, 2))
    SistemaWeb = Column(SmallInteger)
    SistemaEscritorio = Column(SmallInteger)
    SistemaGestion = Column(SmallInteger)
    idComisionista2 = Column(Integer)
    idGiroComercial = Column(Integer)
    PorcentajeDescuento = Column(Numeric(18, 4))
    ClaveEstado = Column(String(3))
    ClavePais = Column(String(3))
    NumRegIdTrib = Column(String(40))
    idFormaPago = Column(String(10))
    DireccionEntrega = Column(String(500))
    idCanal = Column(Integer)
    idMetodoPago = Column(String(10))
    idCondicionesPago = Column(Integer)
    usoCFDi = Column(String(3))
    SistemaPtoVenta = Column(SmallInteger)
    ObservacionesCliente = Column(String(200))
    CURP = Column(String(18))
    FechaNacimiento = Column(DateTime)
    GesemCloud = Column(SmallInteger)
    Foto = Column(LargeBinary)
    FechaProximoPago = Column(DateTime)
    RegimenFiscalReceptor = Column(String(3))
    RegimenCapital = Column(String(50))
    CodIdentifForestal = Column(String(20))
    OficioAutorizacion = Column(String(20))
    RFN = Column(String(20))
    app = Column(Integer)
    Categoria = Column(String(3))
    Identificador = Column(String(10))
    idClienteZona = Column(Integer)
    idClienteZonaRuta = Column(Integer)
    idSucursal = Column(Integer)

class DescuentoPorFamilia(Base):
    __tablename__ = 'DescuentoPorFamilia'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idCliente = Column(Integer, nullable=False)
    idTipoProducto = Column(Integer, nullable=False)
    idTipoProductoDetalle = Column(Integer, nullable=False)
    DescuentoAutorizado = Column(Numeric(18, 6), nullable=False)
    idUsuario = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)

class Compras(Base):
    __tablename__ = 'Compras'
    idCompra = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idTipoDocumento = Column(Integer, nullable=False)
    idProveedor = Column(Integer)
    FolioCompra = Column(Integer)
    FormaPago = Column(String(50))
    MetodoPago = Column(String(50))
    Folio = Column(String(40))
    Fecha = Column(DateTime, nullable=False)
    SubTotal = Column(Numeric(18, 6))
    Descuento = Column(Numeric(18, 6))
    IVA = Column(Numeric(18, 6))
    Total = Column(Numeric(18, 6))
    Observaciones = Column(String(500))
    Estatus = Column(String(1), nullable=False)
    FechaCancelacion = Column(DateTime)
    RutaXML = Column(String(500))
    RutaPDF = Column(String(500))
    idUsuario = Column(Integer)
    IEPS = Column(Numeric(18, 6))
    idMoneda = Column(Integer)
    idTipoGasto = Column(Integer)
    FechaCaptura = Column(DateTime)
    PorcientoUtilidad = Column(Numeric(14, 6))
    idAlmacen = Column(Integer)
    idCondicionesPago = Column(Integer)
    FechaVencimientoCredito = Column(DateTime)
    idObra = Column(Integer)
    TotalLetras = Column(String(-1))
    idTipoGastoDetalle = Column(Integer)
    app = Column(Integer)
    MercanciaFisica = Column(Integer)
    FechaMercanciaFisica = Column(DateTime)
    ImporteRetIVA = Column(Numeric(14, 6))
    ImporteISR = Column(Numeric(14, 6))
    UtilizadoNotaCredito = Column(Numeric(18, 6))
    DescuentoComercial = Column(Numeric(18, 6))

class Tallas(Base):
    __tablename__ = 'Tallas'
    idTalla = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Talla = Column(String(50), nullable=False)

class MovimientosTimbres(Base):
    __tablename__ = 'MovimientosTimbres'
    idMovimientoTimbre = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresaTimbre = Column(Integer, nullable=False)
    idFactura = Column(Integer, nullable=False)
    UUID = Column(String(50))
    Estatus = Column(String(1), nullable=False)
    Fecha = Column(DateTime, nullable=False)
    app = Column(Integer)

class EC_Domicilio(Base):
    __tablename__ = 'EC_Domicilio'
    idDomicilio = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idUsuario = Column(Integer)
    Calle = Column(String(150))
    NumeroExterior = Column(String(50))
    NumeroInterior = Column(String(50))
    Colonia = Column(String(100))
    Localidad = Column(String(100))
    Referencia = Column(String(100))
    Municipio = Column(String(100))
    Estado = Column(String(100))
    Pais = Column(String(100))
    CodigoPostal = Column(String(6))
    Contacto = Column(String(100))
    Telefonos = Column(String(100))
    Facturacion = Column(String(1))
    clavePais = Column(String(10))
    claveEstado = Column(String(10))

class TipoOperacion(Base):
    __tablename__ = 'TipoOperacion'
    idTipoOperacion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    TipoOperacion = Column(String(50), nullable=False)

class FacturasComplementoCartaPorteMercanciasTranspFerroviario(Base):
    __tablename__ = 'FacturasComplementoCartaPorteMercanciasTranspFerroviario'
    idComplementoCartaPorteMercanciasTranspFerroviario = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorteMercancias = Column(Integer, nullable=False)
    TipoDeServicioFerroviario = Column(String(5), nullable=False)
    NombreAsegFerroviario = Column(String(50), nullable=False)
    NumPolizaSeguroFerroviario = Column(String(30), nullable=False)
    TipoDeTrafico = Column(String(10))

class PacienteObservaciones(Base):
    __tablename__ = 'PacienteObservaciones'
    idPacienteObservaciones = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idPaciente = Column(Integer, nullable=False)
    Observaciones = Column(String(250), nullable=False)
    Fecha = Column(DateTime, nullable=False)
    idUsuario = Column(Integer, nullable=False)
    RutaDocumento = Column(String(1000))

class Colores(Base):
    __tablename__ = 'Colores'
    idColor = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Color = Column(String(50), nullable=False)

class CONTA_Configuracion(Base):
    __tablename__ = 'CONTA_Configuracion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idEmpresa = Column(Integer, nullable=False)
    DecimalesCantidad = Column(Integer)
    DecimalesPrecio = Column(Integer)
    AplicaIVA = Column(Integer)
    ManejaSerie = Column(Integer)
    ProductosWEB = Column(Integer)
    PermiteVentaNegativos = Column(Integer)
    idFormaPagoDefault = Column(String(2))
    idMetodoPagoDefault = Column(String(3))
    idCondicionesPagoDefault = Column(Integer)
    ImprimeDetallePaquete = Column(Integer)
    SeleccionarFormatoGas = Column(Integer)
    CantidadCopiasTicket = Column(Integer)
    TieneNomina = Column(Integer)
    SNCF = Column(Integer)
    RedondeaPrecio = Column(Integer)
    TieneComplemento = Column(Integer)
    TieneAddenda = Column(Integer)
    TienePoliza = Column(Integer)
    idUsoCFDiDefault = Column(String(3))
    MostrarPreciosConImpuestos = Column(Integer)
    BusquedaPorCodigoBarras = Column(Integer)
    LeerXMLCompras = Column(Integer)
    CombosCliente = Column(Integer)
    PedidosPuntoVenta = Column(Integer)
    FolioPedidoPorUsuario = Column(Integer)
    DescuentoPorImporte = Column(Integer)
    idFormatoCFDi = Column(Integer)
    ComisionesFacturaPagada = Column(Integer)
    DiasVigenciaPedido = Column(Integer)
    ReporteFacturasEmitidas = Column(Integer)
    ReporteCobrosRealizados = Column(Integer)
    ReportePagosRealizados = Column(Integer)
    ReporteMovimientoProductos = Column(Integer)
    ProductosDebajoMinimo = Column(Integer)
    CostoVendido = Column(Integer)
    CostoAlmacen = Column(Integer)
    ResumenEjecutivo = Column(Integer)
    GraficaBancos = Column(Integer)
    OtrosPreciosPorciento = Column(Integer)
    MostrarTimbres = Column(Integer)
    ComplementoPagoEnCobros = Column(Integer)
    DividirFacturas = Column(Integer)
    Premium = Column(Integer)
    idFormatoTicket = Column(Integer)
    idFormatoEstimaciones = Column(Integer)
    idFormatoCotizaciones = Column(Integer)
    ControlObras = Column(Integer)
    CostoPromedio = Column(Integer)
    MultiEmpresaCompartida = Column(Integer)
    esTransportista = Column(Integer)
    CantidadTickets = Column(Integer)
    ActivarEdicionPOS = Column(Integer)
    CantidadCopiasTicketPedido = Column(Integer)
    idFormatoNotaVenta = Column(Integer)
    PuertoBascula = Column(String(5))
    VentasDebajoCosto = Column(Integer)
    PonerMotivoDescuento = Column(Integer)
    idFormatoRemision = Column(Integer)
    ImprimirSurtido = Column(Integer)
    ModuloVehicular = Column(Integer)
    SumarProductosIguales = Column(Integer)
    ModuloRestaurante = Column(Integer)
    PorcientoComisionTC = Column(Numeric(18, 2))
    FacturarNotasVenta = Column(Integer)
    LimiteEfectivoCaja = Column(Numeric(18, 2))
    EliminaImpuestosFacturaGlobal = Column(Integer)
    EliminaPartePaquete = Column(Integer)
    ListarProductosClientes = Column(Integer)
    MostrarTara = Column(Integer)
    ModificarCosto = Column(Integer)
    ConectaInternet = Column(Integer)
    AutoFactura = Column(Integer)
    idFormatoCompra = Column(Integer)
    PermiteExportarCambioPrecios = Column(Integer)
    BaseDatosNube = Column(Integer)
    ConvertiraPesos = Column(Integer)
    PrecioPorNumero = Column(Integer)
    CantidadCaracteresBusqueda = Column(Integer)
    CantidadLetrasIngles = Column(Integer)
    VendedorPorUsuario = Column(Integer)
    PorcentajeMoratorio = Column(Numeric(18, 2))
    PagoServicios = Column(Integer)
    ComisionTiempoAire = Column(Numeric(18, 2))
    ComisionServicio = Column(Numeric(18, 2))
    VentaPrecioCeros = Column(Integer)
    HuellaDigital = Column(Integer)
    GYM = Column(Integer)
    VerificadorPreciosAislado = Column(Integer)
    SurtirPedidoIncompleto = Column(Integer)
    CartaPorte = Column(Integer)
    ImprimirPedidoPuntoVenta = Column(Integer)
    PtoVentaMostrarColumnaDescuento = Column(Integer)
    PtoVentaMostrarColumnaPedimento = Column(Integer)
    PromocionFamilia = Column(Integer)
    SucursalComoEmpresa = Column(Integer)
    TipoTransporte = Column(Integer)
    ComercioExterior = Column(Integer)
    PantallaTouch = Column(Integer)
    ModuloRestauranteFormato = Column(Integer)
    FacturarNotasVentaDias = Column(Integer)
    FacturarNotasVentaMesAnterior = Column(Integer)
    ImprimirPropinaSugerida = Column(Integer)
    ModuloFarmacia = Column(Integer)
    AutoguardadoTicket = Column(Integer)
    Maderera = Column(Integer)
    CargaProductos = Column(Integer)
    FarmaciaFolioReceta = Column(Integer)
    HorarioNocheInicio = Column(Integer)
    HorarioNocheFin = Column(Integer)
    ListaPrecioNoche = Column(Integer)
    AcumulacionPuntos = Column(Integer)
    ValorPuntosDinero = Column(Numeric(18, 4))
    PorcentajeVentaEnPuntos = Column(Integer)
    PuntosPorProducto = Column(Integer)
    EditarEstimaciones = Column(Integer)
    TieneMonedero = Column(Integer)
    UsaSaldoFavor = Column(Integer)
    idCuentaDestinoSaldoFavor = Column(Integer)
    BasculaPorFamilia = Column(Integer)
    idComisionPorVenta = Column(Integer)
    idCorteViejo = Column(Integer)
    PtoVentaAplicarDebito = Column(Integer)
    TieneVisor = Column(Integer)

class FacturasComplementoCartaPorteMercancias(Base):
    __tablename__ = 'FacturasComplementoCartaPorteMercancias'
    idComplementoCartaPorteMercancias = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorte = Column(Integer, nullable=False)
    PesoBrutoTotal = Column(Numeric(18, 3))
    UnidadPeso = Column(String(10))
    PesoNetoTotal = Column(Numeric(18, 3))
    NumTotalMercancias = Column(Integer)
    CargoPorTasacion = Column(Numeric(18, 2))
    LogisticaInversaRecoleccionDevolucion = Column(String(2))

class EC_Carrito(Base):
    __tablename__ = 'EC_Carrito'
    idCarrito = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idUsuario = Column(Integer)
    idUsuarioTemporal = Column(String(8), nullable=False)
    Estatus = Column(String(1))
    fechaCreacion = Column(DateTime)
    fechaModificacion = Column(DateTime)

class CotizacionesDetalle(Base):
    __tablename__ = 'CotizacionesDetalle'
    idCotizacionDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCotizacion = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Cantidad = Column(Numeric(18, 6), nullable=False)
    Precio = Column(Numeric(18, 6), nullable=False)
    PorcentajeDescuento = Column(Numeric(18, 6), nullable=False)
    IvaDetalle = Column(Numeric(18, 6))
    ObservacionesDetalle = Column(String(1000))
    Costo = Column(Numeric(18, 6))
    ImprimirImagen = Column(Integer)
    IEPSDetalle = Column(Numeric(18, 6))
    PorcientoIVA = Column(Numeric(18, 6))
    PorcientoIEPS = Column(Numeric(18, 6))
    Exento = Column(Integer)
    PrecioFinal = Column(Numeric(18, 6))
    SubTotalSinDescuentoDetalle = Column(Numeric(18, 6))
    DescuentoDetalle = Column(Numeric(18, 6))
    SubTotalConDescuentoDetalle = Column(Numeric(18, 6))
    TotalDetalle = Column(Numeric(18, 6))
    LargoCristal = Column(Numeric(18, 4))
    AnchoCristal = Column(Numeric(18, 4))
    esServicioCristal = Column(SmallInteger)
    Lado1 = Column(Numeric(18, 4))
    Lado2 = Column(Numeric(18, 4))
    Lado3 = Column(Numeric(18, 4))
    Lado4 = Column(Numeric(18, 4))
    esPaquete = Column(Integer)
    FactorExistencia = Column(Numeric(18, 6))
    DescripcionProducto = Column(String(1000))
    RetIVA = Column(Numeric(18, 6))
    ISR = Column(Numeric(18, 6))
    PorcientoRetIVA = Column(Numeric(18, 6))
    PorcientoISR = Column(Numeric(18, 6))

class NOMINA_PlantillaReciboOtroPago(Base):
    __tablename__ = 'NOMINA_PlantillaReciboOtroPago'
    idPlantillaReciboOtroPago = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idPlantillaRecibo = Column(Integer, nullable=False)
    TipoOtroPago = Column(String(3), nullable=False)
    ClaveOtroPago = Column(String(15), nullable=False)
    ConceptoOtroPago = Column(String(100), nullable=False)
    ImporteOtroPago = Column(Numeric(18, 6), nullable=False)
    SubsidioCausado = Column(Numeric(18, 6))
    SaldoAFavor = Column(Numeric(18, 6))
    Anno = Column(Integer)
    RemanenteSalFav = Column(Numeric(18, 6))

class FacturasComplementoCartaPorteMercanciasTranspFerroviarioDerechoPaso(Base):
    __tablename__ = 'FacturasComplementoCartaPorteMercanciasTranspFerroviarioDerechoPaso'
    idComplementoCartaPorteMercanciasTranspFerroviarioDerechoPaso = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorteMercanciasTranspFerroviario = Column(Integer, nullable=False)
    TipoDerechoDePaso = Column(String(10), nullable=False)
    KilometrajePagado = Column(Numeric(18, 2), nullable=False)

class ProductosTallaColor(Base):
    __tablename__ = 'ProductosTallaColor'
    idProductoTallaColor = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer, nullable=False)
    idTalla = Column(Integer)
    idColor = Column(Integer)
    ExistenciaTallaColor = Column(Numeric(14, 4))
    Codigo = Column(String(50))
    idFactura = Column(Integer)
    idCompra = Column(Integer)
    CodigoBarras = Column(LargeBinary)
    Estatus = Column(String(1))

class EC_CarritoDetalle(Base):
    __tablename__ = 'EC_CarritoDetalle'
    idCarritoDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCarrito = Column(Integer)
    idProducto = Column(Integer)
    Cantidad = Column(Numeric(18, 6))
    Precio = Column(Numeric(18, 6))
    fechaRegistro = Column(DateTime)

class FacturasComplementoCartaPorteMercanciasTranspMaritimoRemolqueCCP(Base):
    __tablename__ = 'FacturasComplementoCartaPorteMercanciasTranspMaritimoRemolqueCCP'
    idComplementoCartaPorteMercanciasTranspMaritinoRemolqueCCP = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorteMercanciasTranspMaritino = Column(Integer, nullable=False)
    SubTipoRemCCP = Column(String(10), nullable=False)
    PlacaCCP = Column(String(10), nullable=False)

class Doctores(Base):
    __tablename__ = 'Doctores'
    idDoctor = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Nombre = Column(String(300), nullable=False)
    Direccion = Column(String(500))
    Telefonos = Column(String(100), nullable=False)
    Cedula = Column(String(50))
    InstitutoTituloProfesional = Column(String(300))
    EspecialidadMedico = Column(String(100))
    idUsuario = Column(Integer)

class CuentasBancos(Base):
    __tablename__ = 'CuentasBancos'
    idCuentaBanco = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idBanco = Column(Integer, nullable=False)
    NumeroCuenta = Column(String(50), nullable=False)
    Observaciones = Column(String(150))
    Saldo = Column(Numeric(18, 2), nullable=False)
    FechaApertura = Column(DateTime)
    Estatus = Column(String(1))

class NOMINA_TipoIncapacidad(Base):
    __tablename__ = 'NOMINA_TipoIncapacidad'
    idTipoIncapacidad = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveTipoIncapacidad = Column(String(3), nullable=False)
    TipoIncapacidad = Column(String(100), nullable=False)

class FacturasAduanaDetalle(Base):
    __tablename__ = 'FacturasAduanaDetalle'
    idFacturaAduanaDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    Trafico = Column(String(150))
    Pedimento = Column(String(150))
    FechaPedimento = Column(DateTime)
    EmbarcadoPor = Column(String(150))
    Bultos = Column(Integer)
    Peso = Column(Numeric(18, 4))
    Mercancia = Column(String(150))
    Proveedor = Column(String(150))
    Factura = Column(String(150))
    TipoOperacion = Column(String(150))
    ImporteTotal = Column(Numeric(18, 2))
    ConceptoUno = Column(String(50))
    ConceptoDos = Column(String(50))
    ConceptoTres = Column(String(50))
    ConceptoCuatro = Column(String(50))
    ImporteUno = Column(Numeric(18, 2))
    ImporteDos = Column(Numeric(18, 2))
    ImporteTres = Column(Numeric(18, 2))
    ImporteCuatro = Column(Numeric(18, 2))
    Remesa = Column(Numeric(18, 2))
    TipoCambioPed = Column(Numeric(18, 6))
    GMasterGHouse = Column(String(50))
    FacturaUno = Column(String(50))
    FacturaDos = Column(String(50))
    FacturaTres = Column(String(50))
    FacturaCuatro = Column(String(50))
    ClienteImporteUno = Column(Numeric(18, 2))
    ClienteImporteDos = Column(Numeric(18, 2))
    ClienteImporteTres = Column(Numeric(18, 2))
    ClienteImporteCuatro = Column(Numeric(18, 2))

class PedidosCliente(Base):
    __tablename__ = 'PedidosCliente'
    idPedidoCliente = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    idCliente = Column(Integer, nullable=False)
    NumeroPedidoCliente = Column(String(50), nullable=False)
    Fecha = Column(DateTime, nullable=False)
    PorcentajeDescuento = Column(Numeric(18, 6))
    SubTotalAntesDescuento = Column(Numeric(18, 6))
    ImporteDescuento = Column(Numeric(18, 6))
    ImporteIVA = Column(Numeric(18, 6))
    Observaciones = Column(String(500))
    idFactura = Column(String(500))
    idUsuario = Column(Integer)
    RutaPDF = Column(String(500))
    CantidadLetra = Column(String(250))
    NombreCliente = Column(String(150))
    ImporteIEPS = Column(Numeric(18, 6))
    Estatus = Column(String(1))
    idVendedor = Column(Integer)
    EC_cuentaPago = Column(String(100))
    EC_fechaPago = Column(DateTime)
    EC_idDomicilio = Column(Integer)
    EC_noTransaccionPago = Column(String(100))
    EC_totalPago = Column(Numeric(18, 2))
    EC_usuario = Column(Integer)
    EC_web = Column(Integer)
    EC_estatus = Column(String(20))
    EC_observaciones = Column(String(500))
    GD_web = Column(Integer)
    ClavePedido = Column(String(20))
    idMoneda = Column(Integer)
    EC_facturar = Column(Integer)
    SurteParcialmente = Column(Integer)
    DiasVigenciaPedido = Column(Integer)
    idFormaEnvio = Column(Integer)
    DireccionEnvio = Column(String(1000))
    FechaPromesa = Column(DateTime)
    ImporteRetIVA = Column(Numeric(18, 6))
    ImporteISR = Column(Numeric(18, 6))

class ClienteSaldoFavor(Base):
    __tablename__ = 'ClienteSaldoFavor'
    idClienteSaldoFavor = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCliente = Column(Integer)
    Saldo = Column(Numeric(18, 2))
    FechaCreacion = Column(DateTime)

class FacturasComplementoCartaPorteMercanciasTranspFerroviarioCarro(Base):
    __tablename__ = 'FacturasComplementoCartaPorteMercanciasTranspFerroviarioCarro'
    idComplementoCartaPorteMercanciasTranspFerroviarioCarro = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorteMercanciasTranspFerroviario = Column(Integer, nullable=False)
    TipoCarro = Column(String(5), nullable=False)
    MatriculaCarro = Column(String(15), nullable=False)
    GuiaCarro = Column(String(15), nullable=False)
    ToneladasNetasCarro = Column(Numeric(18, 3), nullable=False)

class EC_Config(Base):
    __tablename__ = 'EC_Config'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idListaPrecioEC = Column(Integer)
    mostrarSinExistencia = Column(Integer)
    mostrarExistencia = Column(Integer)

class Pagos(Base):
    __tablename__ = 'Pagos'
    idPago = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCompra = Column(Integer, nullable=False)
    idTipoOperacion = Column(Integer, nullable=False)
    idBanco = Column(Integer)
    Fecha = Column(DateTime, nullable=False)
    Cantidad = Column(Numeric(18, 2), nullable=False)
    NumeroDocumento = Column(String(150))
    idUsuario = Column(Integer)
    idCuentaBanco = Column(Integer)
    FechaCaptura = Column(DateTime)
    NombreBeneficiarioCheque = Column(String(100))
    RFCBeneficiarioCheque = Column(String(13))
    FolioDocumento = Column(String(50))
    RFCProveedor = Column(String(15))
    Verificado = Column(Boolean)
    app = Column(Integer)
    idNotadeCredito = Column(Integer)

class FacturasDetalleReceta(Base):
    __tablename__ = 'FacturasDetalleReceta'
    idFacturasDetalleReceta = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    idDoctor = Column(Integer, nullable=False)
    NumeroReceta = Column(String(50))
    idProducto = Column(Integer)
    Cantidad = Column(Numeric(18, 6))
    TratamientoCompleto = Column(Integer)
    ObservacionesReceta = Column(String(500))

class MS_ServicioCliente(Base):
    __tablename__ = 'MS_ServicioCliente'
    idServicioCliente = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCliente = Column(Integer)
    Calle = Column(String(100))
    noInt = Column(String(50))
    noExt = Column(String(50))
    Colonia = Column(String(100))
    codigoPostal = Column(String(6))
    Estado = Column(String(50))
    Ciudad = Column(String(50))
    Contacto = Column(String(100))
    Descripcion = Column(String(500))
    idUsuarioAsignado = Column(Integer)
    fechaServicio = Column(DateTime)
    idEstatus = Column(Integer)
    fechaCreacion = Column(DateTime)
    idUsuarioCreo = Column(Integer)
    numeroServicio = Column(Integer)
    idEmpresa = Column(Integer)
    idUsuarioModifico = Column(Integer)
    Observaciones = Column(String(500))

class FacturasComplementoCartaPorteMercanciasTranspFerroviarioCarroContenedor(Base):
    __tablename__ = 'FacturasComplementoCartaPorteMercanciasTranspFerroviarioCarroContenedor'
    idComplementoCartaPorteMercanciasTranspFerroviarioCarroContenedor = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idComplementoCartaPorteMercanciasTranspFerroviarioCarro = Column(Integer, nullable=False)
    TipoContenedor = Column(String(5), nullable=False)
    PesoContenedorVacio = Column(Numeric(18, 3), nullable=False)
    PesoNetoMercancia = Column(Numeric(18, 3), nullable=False)

class ClienteSaldoFavorMovimientos(Base):
    __tablename__ = 'ClienteSaldoFavorMovimientos'
    idClienteSaldoFavorMovimiento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idClienteSaldoFavor = Column(Integer)
    Importe = Column(Numeric(18, 2))
    Fecha = Column(DateTime)
    idFactura = Column(Integer)
    idOperacionCaja = Column(Integer)
    idMovimientoCuentaBanco = Column(Integer)
    formaPago = Column(String(50))

class RET_ComplementoPagoExtranjeros(Base):
    __tablename__ = 'RET_ComplementoPagoExtranjeros'
    idRetComplemento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCFDIRetencion = Column(Integer)
    EsBeneficiario = Column(Integer)
    BenRFC = Column(String(20))
    BenCURP = Column(String(20))
    BenRazonSocial = Column(String(255))
    BenConcepto = Column(Integer)
    BenDescripcion = Column(String(255))
    NoBenPais = Column(String(3))
    NoBenConcepto = Column(Integer)
    NoBenDescripcion = Column(String(255))

class FacturasCFDiRelacionados(Base):
    __tablename__ = 'FacturasCFDiRelacionados'
    idCFDiRelacionado = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    idFacturaRelacionada = Column(Integer)
    Folio = Column(String(50), nullable=False)
    UUID = Column(String(50), nullable=False)
    TipoRelacion = Column(String(2))

class ClaveProdServ(Base):
    __tablename__ = 'ClaveProdServ'
    idClaveProdServ = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveProdServ = Column(String(10), nullable=False)
    DescripcionClaveProdServ = Column(String(150), nullable=False)

class FacturaDetalleComision(Base):
    __tablename__ = 'FacturaDetalleComision'
    idFacturaDetalleComision = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idFactura = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    ComisionPrecio = Column(Numeric(18, 6), nullable=False)
    MontoMetaPrecio = Column(Numeric(18, 6), nullable=False)

class PedidosClienteDetalle(Base):
    __tablename__ = 'PedidosClienteDetalle'
    idPedidoClienteDetalle = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idPedidoCliente = Column(Integer, nullable=False)
    idProducto = Column(Integer, nullable=False)
    Cantidad = Column(Numeric(18, 4), nullable=False)
    Precio = Column(Numeric(18, 6))
    PorcentajeDescuento = Column(Numeric(18, 6))
    IvaDetalle = Column(Numeric(18, 6))
    ObservacionesDetalle = Column(String(1000))
    Descripcion = Column(String(1000))
    PorcientoIVA = Column(Numeric(18, 6))
    PorcientoIEPS = Column(Numeric(18, 6))
    IEPSDetalle = Column(Numeric(18, 6))
    Exento = Column(Integer)
    PrecioFinal = Column(Numeric(18, 6))
    SubTotalSinDescuentoDetalle = Column(Numeric(18, 6))
    DescuentoDetalle = Column(Numeric(18, 6))
    SubTotalConDescuentoDetalle = Column(Numeric(18, 6))
    TotalDetalle = Column(Numeric(18, 6))
    esPaquete = Column(Integer)
    idProductoSeries = Column(String(500))
    Surtido = Column(Numeric(18, 4))
    SurtirTMP = Column(Numeric(18, 4))
    FactorExistencia = Column(Numeric(18, 6))
    idProductoTallas = Column(String(500))
    RetIVA = Column(Numeric(18, 6))
    ISR = Column(Numeric(18, 6))
    PorcientoRetIVA = Column(Numeric(18, 6))
    PorcientoISR = Column(Numeric(18, 6))

class SERVICIOS_Productos(Base):
    __tablename__ = 'SERVICIOS_Productos'
    idProducto = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Bolsa = Column(String(200))
    Categoria = Column(String(200))
    CategoriaID = Column(Integer)
    BolsaID = Column(Integer)
    Carrier = Column(String(200))
    CarrierID = Column(Integer)
    Codigo = Column(String(20))
    Monto = Column(Numeric(18, 2))
    Unidades = Column(Numeric(18, 2))
    Vigencia = Column(String(200))
    Descripcion = Column(String(-1))
    Estatus = Column(String(1))

class FacturasConstConceptos(Base):
    __tablename__ = 'FacturasConstConceptos'
    idFacturaConstConcepto = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idEmpresa = Column(Integer, nullable=False)
    IdentificadorConcepto = Column(String(10), nullable=False)
    Descripcion = Column(String(500), nullable=False)

class MovimientosCuentaBanco(Base):
    __tablename__ = 'MovimientosCuentaBanco'
    idMovimientoCuentaBanco = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCuentaBanco = Column(Integer, nullable=False)
    Fecha = Column(DateTime, nullable=False)
    idCobro = Column(Integer)
    Deposito = Column(Numeric(18, 2), nullable=False)
    idPago = Column(Integer)
    Retiro = Column(Numeric(18, 2), nullable=False)
    Observaciones = Column(String(100))
    idGasto = Column(Integer)
    RecibidoUSD = Column(Numeric(18, 2))
    TipoCambio = Column(Numeric(18, 2))

class RestaurantComplementos(Base):
    __tablename__ = 'RestaurantComplementos'
    idRestaurantComplemento = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idProducto = Column(Integer, nullable=False)

class RET_CatalogoTipoContribuyenteSujetoRetencion(Base):
    __tablename__ = 'RET_CatalogoTipoContribuyenteSujetoRetencion'
    idTipoContribuyenteSujetoRetencion = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    ClaveTipoContribuyenteSujetoRetencion = Column(String(2), nullable=False)
    DescripcionTipoContribuyenteSujetoRetencion = Column(String(100), nullable=False)

class ClienteEntrega(Base):
    __tablename__ = 'ClienteEntrega'
    idClienteEntrega = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    idCliente = Column(Integer, nullable=False)
    Direccion = Column(String(1000), nullable=False)
    Contacto = Column(String(100))
    Telefono = Column(String(100))

