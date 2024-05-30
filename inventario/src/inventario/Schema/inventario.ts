import { Schema } from 'mongoose';

export const InventarioSchema = new Schema({
  nombre: { type: String, required: true },
  descripcion: String,
  cantidad: { type: Number, required: true },
  precio: { type: Number, required: true },
});
