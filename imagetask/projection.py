class Projection( object ):

	def __init__( self, geod, start_lat, start_lon, scaleX, scaleY ):
		self._geod = geod

		self.start_lat = start_lat
		self.start_lon = start_lon
		self.scaleX = scaleX
		self.scaleY = scaleY

	def to_xy( self, lat, lon ):

		#assert( lat > self.start_lat )
		#assert( lon > self.start_lon )

		_, _, dlat = self._geod.inv( self.start_lon, lat, lon, lat )
		_, _, dlon = self._geod.inv( lon, self.start_lat, lon, lat )

		dx = int( dlat / self.scaleX )
		dy = int( dlon / self.scaleY )

		return dx, dy

	def to_latlon( self, x, y ):
		lon, lat, _ = self._geod.fwd( self.start_lon, self.start_lat, 180, y * self.scaleY )
		lon, lat, _ = self._geod.fwd( lon, lat, 90, x * self.scaleX )
		return lat, lon


# proj = ImageProj(
# 	geod=pyproj.Geod( ellps='WGS84' ),
# 	start_lat=55.9146,
# 	start_lon=37.3151,
# 	scale=50,
# 	)
