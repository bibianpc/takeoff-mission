# Fecha actual
year=$(date +%Y)
month=$(date +%m)
day=$(date +%d)

hoy=$year"-"$month"-"$day

mkdir devices
mkdir logsapollo11
mkdir config
mkdir stats

chmod 777 logsapollo11
chmod 777 stats

#Log
cd logsapollo11
fecha_actual=$(date)
echo "${fecha_actual}: Apollo11 Inicia" >> "APL-${hoy}.log"
cd ..


PROYECTOS=("ORB" "CNL" "MRS" "DES")

# Posibles estados de los satelites
ESTADOS=("unknown" "excelent" "good" "warning" "kill")

cd devices

# Se elimina y se crea la carpeta con la fecha de hoy
rm -r $hoy
mkdir $hoy
chmod 777 $hoy

cd $hoy

for i in {1..100}
do
	# Calculamos una posicion aleatoria entre 0 y 4 de la lista de estados para enviarla al archivo.
	estado_aleatorio=$((0 + $RANDOM % 5))
	# Calculamos una posicion aleatoria entre 0 y 3 de la lista de siglas de proyecto para nombrar al archivo.
	sigla_aleatoria=$((0 + $RANDOM % 4))
	sigla=${PROYECTOS[sigla_aleatoria]}

	iteracion=`printf %04d $i`
	
	echo ${ESTADOS[estado_aleatorio]} >> "APL${sigla}-${iteracion}.log"
	
	# Verificamos a cual sigla corresponde la generada aleatoriamente
	if [ $sigla = "ORB" ]
	then		
		chmod 777 "APL${sigla}-${iteracion}.log"
	fi
	
	cd ../../
	cd logsapollo11
	fecha_actual=$(date)
	echo "${fecha_actual}: Se crea archivo APL${sigla}-${iteracion}.log" >> "APL-${hoy}.log"
	cd ../
	cd devices
	cd $hoy
done

cd ../..
cd logsapollo11
fecha_actual=$(date)
echo "${fecha_actual}: Apollo11 Finaliza" >> "APL-${hoy}.log"

