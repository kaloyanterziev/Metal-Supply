<template>
  <div class="modal fade" tabindex="-1" role="dialog" ref="add-record-modal" id="add-record-modal">
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLongTitle">Add Record</h5>
          <button type="button" ref="close" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body card p-4">
          <form name="form" @submit.prevent="addRecord">
            <div v-if="!successful">
              <div class="form-group">
                <label for="record.material_origin">Material Origin</label>
                <select v-model="record.material_origin" name="record.material_origin" required type="text" class="form-control">
                  <option value="" selected disabled>Please select material origin</option>
                  <option>#1 Bare Bright Copper Wire</option>
                  <option>#1 Copper Tubing</option>
                  <option>#1 Flashing Copper</option>
                  <option>#2 Copper Tubing</option>
                  <option>#2/3 Mix Copper</option>
                  <option>#3 Copper with Tar</option>
                  <option>#3 Roofing Copper</option>
                  <option>17-4 Stainless Steel</option>
                  <option>300 Series Stainless Steel</option>
                  <option>304 Stainless Steel</option>
                  <option>310 Stainless Steel</option>
                  <option>316 Stainless Steel</option>
                  <option>321 Stainless Steel</option>
                  <option>400 Series Stainless Steel</option>
                  <option>500/750 Insulated Cable</option>
                  <option>ACR</option>
                  <option>ACR Ends</option>
                  <option>AL Extrusion</option>
                  <option>AL Thermopane</option>
                  <option>AL/ Copper Rads w/Iron</option>
                  <option>AL/Copper Cutoffs</option>
                  <option>Alternators</option>
                  <option>Aluminum #3</option>
                  <option>Aluminum 6061</option>
                  <option>Aluminum 6063</option>
                  <option>Aluminum Boat</option>
                  <option>Aluminum Breakage</option>
                  <option>Aluminum Bumpers</option>
                  <option>Aluminum Cans</option>
                  <option>Aluminum Clips</option>
                  <option>Aluminum Copper Coil</option>
                  <option>Aluminum Copper Radiators</option>
                  <option>Aluminum Diesel Tank</option>
                  <option>Aluminum Engine Block</option>
                  <option>Aluminum Litho</option>
                  <option>Aluminum Radiators</option>
                  <option>Aluminum Rims</option>
                  <option>Aluminum Scrap</option>
                  <option>Aluminum Siding</option>
                  <option>Aluminum Thermo-Pane/Break</option>
                  <option>Aluminum Transformers</option>
                  <option>Aluminum Turnings</option>
                  <option>Aluminum Wire w/Steel</option>
                  <option>Ballasts</option>
                  <option>Bare Bright Copper</option>
                  <option>Brass</option>
                  <option>Brass Hair Wire</option>
                  <option>Brass Heater Cores</option>
                  <option>Brass Pipe</option>
                  <option>Brass Radiators</option>
                  <option>Brass Scrap</option>
                  <option>Brass Shells</option>
                  <option>Brass Turnings</option>
                  <option>Bronze</option>
                  <option>Bronze Turnings</option>
                  <option>Burnt Copper</option>
                  <option>Car/Truck Batteries</option>
                  <option>Carbide</option>
                  <option>Cast Aluminum</option>
                  <option>Catalytic Converters</option>
                  <option>CATV Wire</option>
                  <option>Christmas Lights</option>
                  <option>Circuit Breakers</option>
                  <option>Clean ACR</option>
                  <option>Clean AL Wire</option>
                  <option>Clean AL/Copper Fin</option>
                  <option>Clean Brass Radiators</option>
                  <option>Clean Brass Turnings</option>
                  <option>Clean Roofing Copper</option>
                  <option>Cobalt</option>
                  <option>Communications Wire</option>
                  <option>Composition Scrap</option>
                  <option>Compressors</option>
                  <option>Copper Scrap</option>
                  <option>Copper Transformers</option>
                  <option>Copper Turnings</option>
                  <option>Copper Yokes</option>
                  <option>Die Cast</option>
                  <option>Dirty ACR</option>
                  <option>Dirty AL Extrusion</option>
                  <option>Dirty AL Radiators</option>
                  <option>Dirty AL/Copper Fin</option>
                  <option>Dirty Aluminum Turnings</option>
                  <option>Dirty Brass</option>
                  <option>Dirty Brass Radiators</option>
                  <option>Dirty Roofing Copper</option>
                  <option>Double Insulated Cable</option>
                  <option>EC Wire</option>
                  <option>Electric Motors (Aluminum)</option>
                  <option>Electric Motors (Copper)</option>
                  <option>Elevator Wire</option>
                  <option>Enameled Copper</option>
                  <option>F 75</option>
                  <option>Fire Wire</option>
                  <option>Forktruck Battery</option>
                  <option>FSX 414</option>
                  <option>Fuses</option>
                  <option>Gold</option>
                  <option>Hastelloy Solids</option>
                  <option>Hastelloy Turnings</option>
                  <option>Heliax Wire</option>
                  <option>High Speed Steel</option>
                  <option>Housewire</option>
                  <option>Inconel</option>
                  <option>Inconel 792</option>
                  <option>Inconel 800</option>
                  <option>Inconel 825</option>
                  <option>Insulated Aluminum Wire</option>
                  <option>Insulated Copper Cable</option>
                  <option>Insulated Copper Wire</option>
                  <option>Insulated Steel BX</option>
                  <option>Invar</option>
                  <option>Junkshop Extrusion</option>
                  <option>Kovar</option>
                  <option>Large Foreign Cat</option>
                  <option>Large GM Cat</option>
                  <option>Lead</option>
                  <option>Lead Batteries</option>
                  <option>Lead Coated Copper</option>
                  <option>Lead Shot</option>
                  <option>Lead Wheel Weights</option>
                  <option>Light Copper</option>
                  <option>MarM247</option>
                  <option>Meatballs (Electric Motors)</option>
                  <option>Monel</option>
                  <option>Ni-Cad Batteries</option>
                  <option>Nickel</option>
                  <option>Non Magnetic Stainless Steel</option>
                  <option>O2 Sensors</option>
                  <option>Old Sheet Aluminum</option>
                  <option>Painted Aluminum</option>
                  <option>Pewter</option>
                  <option>Platinum</option>
                  <option>Plumbers Brass</option>
                  <option>Prepared Aluminum</option>
                  <option>Red Brass</option>
                  <option>Refined Rebrass &amp; Copper</option>
                  <option>Regular Domestic Cat</option>
                  <option>Rod Brass</option>
                  <option>Rod Brass Turnings</option>
                  <option>Romex® Wire</option>
                  <option>Sealed Units</option>
                  <option>Semi-Red Brass</option>
                  <option>Sheet Aluminum</option>
                  <option>Silver</option>
                  <option>Silver Plated Copper</option>
                  <option>Small Foreign Cat</option>
                  <option>Small GM Cat</option>
                  <option>Solid Core Heliax</option>
                  <option>Stainless Steel</option>
                  <option>Stainless Steel Breakage</option>
                  <option>Stainless Steel Heatsinks</option>
                  <option>Stainless Steel Kegs</option>
                  <option>Stainless Steel Sinks</option>
                  <option>Stainless Turnings</option>
                  <option>Starters</option>
                  <option>Steel BX</option>
                  <option>Steel Case Batteries</option>
                  <option>THHN Wire</option>
                  <option>Tin Babbit</option>
                  <option>Tin Coated Copper</option>
                  <option>Tin Insulated Copper Wire</option>
                  <option>Unclean Brass Radiators</option>
                  <option>Wire Scrap</option>
                  <option>Wiring Harness</option>
                  <option>Yellow Brass</option>
                  <option>Zinc</option>
                  <option>Zorba</option>
                  <option>#1 Heavy Melting Steel</option>
                  <option>#1 HMS</option>
                  <option>#1 Prepared</option>
                  <option>#1 Steel</option>
                  <option>#2 Heavy Melting Steel</option>
                  <option>#2 HMS</option>
                  <option>#2 Prepared</option>
                  <option>Automobiles</option>
                  <option>Busheling</option>
                  <option>Car w/Tires</option>
                  <option>Cast Iron</option>
                  <option>Complete Car</option>
                  <option>Crushed Cars</option>
                  <option>Dishwashers</option>
                  <option>Dry Automobile</option>
                  <option>Dryers</option>
                  <option>Incomplete Car</option>
                  <option>Light Iron</option>
                  <option>Machine Shop Turning/Iron Borings</option>
                  <option>Plate &amp; Structural Steel</option>
                  <option>Refrigerators</option>
                  <option>Rotors</option>
                  <option>Scrap Iron</option>
                  <option>Shreddable Steel</option>
                  <option>Steel Shavings</option>
                  <option>Tin</option>
                  <option>Uncleaned Auto Cast</option>
                  <option>Unprepared Cast Iron</option>
                  <option>Unprepared HMS</option>
                  <option>Unprepared P&amp;S</option>
                  <option>Washing Machines</option>
                  <option>Water Heaters</option>
                  <option>Wet Automobile</option>
                  <option>Back Panels</option>
                  <option>Backup Batteries</option>
                  <option>Cellphones</option>
                  <option>Computer Wire</option>
                  <option>CPU Chips</option>
                  <option>CRT</option>
                  <option>Empty PC Servers</option>
                  <option>Hard Drive Boards</option>
                  <option>Hard Drives</option>
                  <option>Hard Drives without Boards</option>
                  <option>Ink Cartridges</option>
                  <option>Keyboards</option>
                  <option>Laptops</option>
                  <option>LCD Monitors (not working)</option>
                  <option>LCD Monitors (working)</option>
                  <option>Low Grade Boards</option>
                  <option>Mainframes</option>
                  <option>Memory</option>
                  <option>Mice</option>
                  <option>Motherboards</option>
                  <option>Non-Green PC Board</option>
                  <option>PC Board with Steel</option>
                  <option>PC Boards</option>
                  <option>PC Tower</option>
                  <option>Power Supplies</option>
                  <option>Printers/Fax Machines</option>
                  <option>Servers</option>
                  <option>Speakers</option>
                  <option>Telecom Equipment</option>
                </select>
              </div>
              <div class="form-group">
                <label for="material_type">Material Type</label>
                <select v-model="record.material_type" name="content_metal" required class="form-control">
                  <option value="" selected disabled>Please select metal</option>
                  <option>Dry Bright Copper Wire</option>
                  <option>Clean Flat Copper Electro</option>
                  <option>Clean Copper Tube / New Copper Tube</option>
                  <option>Burnt Wire No 1</option>
                  <option>Greasy Bright Wire</option>
                  <option>Heavy Copper 98%</option>
                  <option>Tinned Copper 98%</option>
                  <option>Heavy Copper 95%</option>
                  <option>Burnt No 2 Wire 94%</option>
                  <option>Thin Gauge Tinned Rope Wire 94%</option>
                  <option>Copper Tanks (Element Free) 92%</option>
                  <option>Braziery Copper 88%</option>
                  <option>Lead Washed Grey Braziery (Steel Free)</option>
                  <option>Copper Elements (From Tanks)</option>
                  <option>Rolled Aluminium</option>
                  <option>Aluminium Wheels / Alloy Wheels</option>
                  <option>Aluminium Cutts (New Production)</option>
                  <option>Clean H9 / HE9</option>
                  <option>Mixed H9 / HE9</option>
                  <option>Painted H9 / HE9</option>
                  <option>Aluminium Quad / Aluminium Wire</option>
                  <option>Cast Aluminium</option>
                  <option>Aluminium Turnings</option>
                  <option>Aluminium Rads / Copper Rads (Steel Free)</option>
                  <option>Irony Aluminium</option>
                  <option>Clean Soft Lead</option>
                  <option>Lead Batteries</option>
                  <option>Lead Zinc Wheel Weights</option>
                  <option>Mixed Brass</option>
                  <option>Brass Borings &amp; Turnings</option>
                  <option>Brass &amp; Copper Compo Rads (Steel Free)</option>
                  <option>Household Cable / VIR 40%</option>
                  <option>Single Cable 65%</option>
                  <option>Wiring Looms 55% (No Fuse board / ECU)</option>
                  <option>Low Grade Cable / Armoured Cable 25%</option>
                  <option>Clean Pyro</option>
                  <option>Plastic Pyro</option>
                  <option>Electric Motors (incl. Starters and Alternators)</option>
                  <option>Zinc / Roofing Zinc</option>
                  <option>18/8 304 Stainless</option>
                  <option>18/8 304 Stainless Turnings</option>
                  <option>18/8 316 Stainless</option>
                  <option>Chrome Iron</option>
                  <option>Gunmetal Scrap</option>
                  <option>Phosphor Bronze</option>
                  <option>CB Rads</option>
                  <option>Gunmetal Turnings</option>
                </select>
              </div>
              <div class="form-group">
                <label for="record.tonnes">Tonnes</label>
                <input v-model="record.tonnes" name="record.tonnes" type="number" required class="form-control" step="any" min="0" />
              </div>
              <div class="form-group">
                <label for="record.latitude">Latitude</label>
                <input v-model="record.latitude" name="record.latitude" type="number" required step="any" min="-90" max="90" class="form-control" />
              </div>
              <div class="form-group">
                <label for="record.longitude">Longitude</label>
                <input v-model="record.longitude" name="record.longitude" type="number" required step="any" min="-180" max="180" class="form-control" />
              </div>
              <div class="form-group">
                <div class="container row justify-content-between">
                  <label for="record.public">Would you like this Record to be publicly visible?</label>
                  <input v-model="record.public" name="record.public" type="checkbox" class="form-control" />
                </div>
              </div>
              <div class="form-group">
                <div class="container row justify-content-between">
                  <label for="contents">Contents</label>
                  <button type="button" class="btn btn-secondary" @click="addEmptyContentToRecord">
                    <font-awesome-icon icon="plus" /> Add Content
                  </button>
                </div>
                <div class="mt-5" v-for="(content, index) in record.contents" v-bind:key="index" >
                  <select v-model="content.metal" name="content_metal" class="form-control">
                    <option value="" selected disabled>Please select metal</option>
                    <option value="Cu">Copper</option>
                    <option value="Al">Aluminum</option>
                    <option value="Pb">Lead</option>
                    <option value="Fe">Iron</option>
                    <option value="Zn">Zinc</option>
                    <option value="Ni">Nickel</option>
                    <option value="Ag">Gold</option>
                    <option value="Au">Silver</option>
                    <option value="Pt">Platinum</option>
                    <option value="Pd">Palladium</option>
                    <option value="Other">Other</option>
                  </select>
                  <div class="container row mt-1">
                    <input class="col-9" v-model="content.percentage" name="content_percentage" type="range" min="0" max="100" />
                    <input class="col-3" v-model="content.percentage" name="content_percentage_text_box" type="number" step="any" min="0" max="100" />
                  </div>
                </div>
              </div>
              <div class="form-group">
                <button type="submit" class="btn btn-primary btn-block" :disabled="loading">
                  <span
                      v-show="loading"
                      class="spinner-border spinner-border-sm"
                  ></span>
                  Create Record
                </button>
              </div>
            </div>
          </form>
          <div
              v-if="message"
              class="alert"
              :class="successful ? 'alert-success' : 'alert-danger'"
          >
            {{ message }}
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import RecordService from '@/services/record.service'

export default {
  name: 'AddRecordModal',
  data() {
    return {
      successful: false,
      loading: false,
      message: "",
      record: {
        contents: [{"percentage": 0, "metal": ""}]
      },
    };
  },
  methods: {
    addRecord() {
      this.message = "";
      this.successful = false;
      this.loading = true;

      let sumOfContentPercentages = this.record.contents.reduce((prev, curr) => prev + curr.percentage, 0)
      if(sumOfContentPercentages>100) {
        this.message = "Contents should not exceed 100%"
        this.loading = false;
        return
      }

      RecordService.createRecord(this.record).then(
          data => {
            this.message = data.data.data;
            this.loading = false;
            this.successful = true;
            const self = this;
            setTimeout(function () {
              self.message = "";
              self.successful = false;
              self.record = {
                contents: [{"percentage": 0, "metal": ""}]
              }
              self.$refs.close.click();
            }, 1000);
            this.$emit('onRecordCreate');
            this.$refs['add-record-modal'].hide();
          }, error => {
            console.log(error)
            this.successful = false;
            this.message = error.data.error;
            this.loading = false;
          }
      );
    },
    addEmptyContentToRecord() {
      this.record.contents.push({"percentage": 0, "metal": ""});
    }
  }
};
</script>

<style scoped>
/*label {*/
/*  display: block;*/
/*  margin-left: 10px;*/
/*}*/

/*.profile-img-card {*/
/*  display: block;*/
/*}*/

/*#hat {*/
/*  position: absolute;*/
/*  top: 1px;*/
/*  right: 1px;*/
/*}*/
</style>