# Contenido AR (país: AR)

- Idioma: español rioplatense (la app traduce a pedido).
- Currículo: Núcleos de Aprendizaje Prioritarios (NAP) y diseños jurisdiccionales; textos originales.
- Nivel 9 (3.er año) y 10 (4.º año): Mathematics ar-mG-NN, Physics ar-pG-NN, Chemistry ar-cG-NN, Biology ar-bG-NN.
- Archivos: banks/<id>.txt, summaries/<id>.json, details/<id>-0K.md; cada lote tiene tools/ar_<lote>_part.json.
- Único archivo compartido que se modifica: index.json (entradas country == "AR"). packs/ y manifest.json los reconstruye el bot.
- Publicación: bash tools/ar_push.sh "mensaje" (pide el token de forma oculta).
